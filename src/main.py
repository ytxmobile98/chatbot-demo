import os.path

from utils.faiss_db import create_faiss_db, db_get_answers_from_query
from utils.split_text import split_file_as_documents


def main():
    data_file = os.path.join(
        os.path.dirname(__file__),
        '../data/sample-answers.txt'
    )
    documents = split_file_as_documents(data_file)

    db = create_faiss_db(documents)

    query = ('留学')
    answers = db_get_answers_from_query(db, query)

    print(answers)


if __name__ == '__main__':
    main()
