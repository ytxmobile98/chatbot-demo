from typing import List

from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter


def split_file_as_documents(filepath: str) -> List[Document]:
    with open(filepath) as f:
        text = f.read()

    splitter = CharacterTextSplitter(
        separator='\n\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    texts = splitter.create_documents([text])

    return texts
