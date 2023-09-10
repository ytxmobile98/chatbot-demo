import os.path

from langchain.vectorstores import FAISS

from utils.faiss_db import create_faiss_db
from utils.split_text import split_file_as_documents


data_file = os.path.join(
    os.path.dirname(__file__),
    '../../data/sample-answers.txt'
)


def create_db() -> FAISS:
    documents = split_file_as_documents(data_file)
    db = create_faiss_db(documents)
    return db
