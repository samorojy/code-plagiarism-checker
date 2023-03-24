import glob
import pygments.util
import psycopg2

from pathlib import Path
from collections import Counter
from database_essentials import get_database_connection
from pygments.token import Token
from pygments.lexers import guess_lexer
from pygments import lex
from typing import Set


def get_tokens(text: str) -> Set[str]:
    lexer = guess_lexer(text)
    return set([token[1] for token in lex(text, lexer) if token[0] in Token.Name])


def put_to_database(conn: psycopg2.extensions.connection, tokens: [str], path: Path):
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO Documents(document_path) VALUES (%s);""", (str(path),))
    cur.execute(f"""SELECT document_id from Documents WHERE document_path=%s;""", (str(path),))
    result = cur.fetchone()
    document_id = result[0]
    for token in tokens:
        cur.execute(f"""INSERT INTO Inverted_Index(token, document_id) VALUES (%s, '{document_id}');""", (token,))


def index_repository(root_path: Path):
    conn = get_database_connection()

    for path in root_path.rglob("*/"):
        print(path)
        if not path.is_dir():
            with open(path) as file:
                try:
                    text = file.read()
                    tokens = get_tokens(text)
                    put_to_database(conn, tokens, path)
                except pygments.util.ClassNotFound:
                    print(f"There is no lexer for {path}")
                except Exception as e:
                    print(f"{e} raised in {path}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    index_repository(Path("educational-plugin-master"))
