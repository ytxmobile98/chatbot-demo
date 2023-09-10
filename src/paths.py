import os.path


data_file_path = os.path.join(
    os.path.dirname(__file__),
    '../data/sample-answers.txt'
)

db_dir = os.path.join(
    os.path.dirname(__file__),
    '../data/faiss.db'
)
db_faiss_file = os.path.join(db_dir, 'index.faiss')
