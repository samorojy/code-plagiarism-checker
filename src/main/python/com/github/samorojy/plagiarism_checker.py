import argparse
import psycopg2
from collections import defaultdict
from indexer import get_tokens
from database_essentials import (
    get_database_connection,
    get_document_by_id,
    get_files_by_token,
)
from typing import Union, Callable

PLAGIARISM_DETECT_ON = 85


def simple_plagiarsim_checker(conn: psycopg2.extensions.connection, tokens: [str]) -> Union[None, str]:
    index = defaultdict(set)
    for token in tokens:
        files = get_files_by_token(conn, token)
        for file in files:
            index[file].add(token)

    plagiarsim_percentage = 0.0
    document_id = None
    for file in index:
        intersection = len(index[file].intersection(tokens))
        current_plagiarism = intersection / len(tokens) * 100
        if current_plagiarism > plagiarsim_percentage:
            plagiarsim_percentage = current_plagiarism
            document_id = file
    if document_id is not None and plagiarsim_percentage >= PLAGIARISM_DETECT_ON:
        file = get_document_by_id(conn, document_id)
        return file
    return None


def check_plagiarism(
    code: str, plagiarism_finder: Callable[[psycopg2.extensions.connection, [str]], Union[None, str]]
) -> str:
    conn = get_database_connection()
    tokens = get_tokens(code)
    plagiarism_find_result = plagiarism_finder(conn, tokens)
    conn.close()
    return plagiarism_find_result


def main() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("code", type=str, help="code to check")
    args = parser.parse_args()
    text = args.code
    result = check_plagiarism(text, simple_plagiarsim_checker)
    if result is not None:
        return result
    return "OK"


if __name__ == "__main__":
    print(main())
