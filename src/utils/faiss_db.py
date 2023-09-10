from typing import List

from langchain.embeddings.base import Embeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS


def create_faiss_db(documents: List[Document],
                    embeddings: Embeddings = OpenAIEmbeddings()) -> FAISS:
    db = FAISS.from_documents(documents, embeddings)
    return db


def db_get_answers_from_query(db: FAISS, query: str) -> List[Document]:
    answers = db.similarity_search(query)
    return answers
