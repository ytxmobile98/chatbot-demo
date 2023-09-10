import gradio as gr

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

from paths import data_file_path, db_dir
from utils.faiss_db import create_db, db_save_local


def init_data(data_file_path: str, db_dir: str):
    db = create_db(data_file_path)
    db_save_local(db, db_dir)


class CounsellingChatBot:
    def __init__(self, pkl_data_dir: str = db_dir, enable_chat: bool = True):
        db = FAISS.load_local(pkl_data_dir, OpenAIEmbeddings())
        llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

        self.SALES_BOT = RetrievalQA.from_chain_type(
            llm,
            retriever=db.as_retriever(
                search_type='similarity_score_threshold',
                search_kwargs={
                    'score_threshold': 0.8
                },
            ),
        )

        self.SALES_BOT.return_source_documents = True

        self.enable_chat = enable_chat


sales_bot = CounsellingChatBot(pkl_data_dir=db_dir)


def chat(message: str, history: str):
    print(f'[message]{message}')
    print(f'[history]{history}')

    ans = sales_bot.SALES_BOT({'query': message})

    if ans['source_documents'] or sales_bot.enable_chat:
        print(ans['result'])
        print(ans['source_documents'])
        return ans['result']
    else:
        return '这个问题我要问问领导'


def launch_gradio():
    demo = gr.ChatInterface(
        fn=chat,
        title='留学咨询',
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name='localhost')


def main():
    init_data(data_file_path, db_dir)
    launch_gradio()


if __name__ == '__main__':
    main()
