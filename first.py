import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pytz
import datetime

global now
now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

st.title("接続テスト")

def on_input_change():
    with st.spinner("送信中。。。"):
        time.sleep(3)
    Human_Agent = "connect" 
    connect = "ok"
    doc_ref = db.collection(user_number).document(str(now))
    doc_ref.set({
        Human_Agent: connect,
    })
    st.write("メッセージの送信が出来ました。接続テストは完了です。")

with st.container():
    user_number = st.text_input("参加者番号を入力して送信ボタンを押してください")
    if user_number:
    # 初期済みでない場合は初期化処理を行う
        if not firebase_admin._apps:
            cred = credentials.Certificate('connecttest-aebb9-firebase-adminsdk-8cfh7-b11eaf48f2.json') 
            default_app = firebase_admin.initialize_app(cred)
        db = firestore.client()
    st.button("送信", on_click=on_input_change)

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
