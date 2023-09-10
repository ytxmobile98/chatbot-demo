import os.path

from typing import List

from langchain.schema import Document

from utils.faiss_db import create_faiss_db, db_get_answers_from_query, \
    db_get_top_k_answers
from utils.split_text import split_file_as_documents


def print_docs(docs: List[Document]):
    for doc in docs:
        print(doc.page_content, '\n', sep='')


def main():
    data_file = os.path.join(
        os.path.dirname(__file__),
        '../data/sample-answers.txt'
    )
    documents = split_file_as_documents(data_file)

    db = create_faiss_db(documents)

    query = ('留学')

    # 1. Get answers for query
    answers = db_get_answers_from_query(db, query)
    print(f'[1. Get answers for query: "{query}"]')
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
