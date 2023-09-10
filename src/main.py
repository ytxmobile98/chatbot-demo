from typing import List

from langchain.schema import Document

from utils.faiss_db import db_get_answers_from_query, db_get_top_k_answers
from utils.import_data import create_db


def print_docs(docs: List[Document]):
    for doc in docs:
        print(doc.page_content, '\n', sep='')


def main():
    db = create_db()

    query = ('留学')

    # 1. Get answers for query
    answers = db_get_answers_from_query(db, query)
    print(f'[1. Get answers for query: "${query}"]')
    print_docs(answers)

    print('\n')

    # 2. Get top k answers for query
    k = 5
    print(f'[2. Get top {k} answers for query: "{query}"]')
    answers = db_get_top_k_answers(db, k, query)
    print_docs(answers)

    print('\n')


if __name__ == '__main__':
    main()
