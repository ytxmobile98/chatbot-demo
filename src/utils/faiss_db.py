from typing import List

from langchain.embeddings.base import Embeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS

from utils.split_text import split_file_as_documents


def create_faiss_db(documents: List[Document],
                    embeddings: Embeddings = OpenAIEmbeddings()) -> FAISS:
    db = FAISS.from_documents(documents, embeddings)
    return db


def create_db(path: str) -> FAISS:
    documents = split_file_as_documents(path)
    db = create_faiss_db(documents)
    return db


def db_save_local(db: FAISS, path: str):
    db.save_local(path)


def db_get_answers_from_query(db: FAISS, query: str) -> List[Document]:
    answers = db.similarity_search(query)
    return answers


def db_get_top_k_answers(db: FAISS, k: int, query: str) -> List[Document]:
    top_k_retriever = db.as_retriever(search_kwargs={'k': k})
    docs = top_k_retriever.get_relevant_documents(query)
    return docs
