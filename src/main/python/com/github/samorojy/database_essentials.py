import psycopg2

DATABASE = "index"
USER = "postgres"
PASSWORD = "postgres"
HOST = "127.0.0.1"
PORT = "5432"


def get_database_connection() -> psycopg2.extensions.connection:
    return psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)


def get_files_by_token(conn: psycopg2.extensions.connection, token: str) -> [str]:
    cur = conn.cursor()
    cur.execute(f"""SELECT document_id from Inverted_Index WHERE token=%s;""", (token,))
    documents_id = cur.fetchall()
    return [stored_data[0] for stored_data in documents_id]


def get_document_by_id(conn: psycopg2.extensions.connection, id: str) -> str:
    cur = conn.cursor()
    cur.execute(f"""SELECT document_path from Documents WHERE document_id='{id}';""")
    return cur.fetchone()[0]
