from typing import List

from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter


def split_file_as_documents(filepath: str) -> List[Document]:
    with open(filepath) as f:
        text = f.read()

    splitter = CharacterTextSplitter(
        separator=r'\d+\.',
        chunk_size=100,
        chunk_overlap=0,
        length_function=len,
        is_separator_regex=True,
    )
    texts = splitter.create_documents([text])

    return texts
