import streamlit as st
import time

st.title("接続テスト")

def on_input_change():
    with st.spinner("送信中。。。"):
        time.sleep(3)
    st.write("メッセージの送信が出来ました。接続テストは完了です。")

with st.container():
    st.text_input("なにか入力して送信ボタンを押してください")
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