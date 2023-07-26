import os
import streamlit as st

from dotenv import load_dotenv
from streamlit_chat import message
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import GitLoader
from langchain.schema import HumanMessage
from langchain.schema import AIMessage

load_dotenv()

# セッション内に保存されたチャット履歴のメモリの取得
try:
    memory = st.session_state["memory"]
except:
    memory = ConversationBufferMemory(return_messages=True)

st.title("langchain for GitHub in Streamlit")
st.caption("by Marthur")

clone_url = st.text_input("GitHubのURLを入力してください")
type = st.text_input("プログラムの種類を入力してください（ex：.kt）")
branch = st.text_input("ブランチを入力してください")
repo_path = "./temp"
read_button = st.button("GitHub読み込み")
user_input = st.text_input("質問を入力してください")
send_button = st.button("送信")

# チャット履歴（HumanMessageやAIMessageなど）を格納する配列の初期化
history = []

if read_button:
    read_button = False
    if os.path.exists(repo_path):
        clone_url = None

    loader = GitLoader(
        clone_url=clone_url,
        branch=branch,
        repo_path=repo_path,
        file_filter=lambda file_path: file_path.endswith(type),
    )

    index = VectorstoreIndexCreator(
        vectorstore_cls=Chroma, # default
        embedding=OpenAIEmbeddings(disallowed_special=()), #default
    ).from_loaders([loader])

    st.session_state["index"] = index
    
    if index :
        memory.chat_memory.add_ai_message("読み込みました")

        # チャット履歴（HumanMessageやAIMessageなど）の読み込み
        try:
            history = memory.load_memory_variables({})["history"]
        except Exception as e:
            st.error(e)

if send_button :
    send_button = False
    memory.chat_memory.add_user_message(user_input)
    index = st.session_state["index"]

    response = index.query(user_input)

    # セッションへのチャット履歴の保存
    st.session_state["index"] = index
    memory.chat_memory.add_ai_message(response)
    st.session_state["memory"] = memory

    # チャット履歴（HumanMessageやAIMessageなど）の読み込み
    try:
        history = memory.load_memory_variables({})["history"]
    except Exception as e:
        st.error(e)

# チャット履歴の表示
for index, chat_message in enumerate(reversed(history)):
    if isinstance(chat_message, HumanMessage):
        message(chat_message.content, is_user=True, key=2 * index)
    elif isinstance(chat_message, AIMessage):
        message(chat_message.content, is_user=False, key=2 * index + 1)
