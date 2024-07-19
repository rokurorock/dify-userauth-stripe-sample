import streamlit as st
from dotenv import load_dotenv
from api.dify import post_chat_message
from streamlit_supabase_auth import login_form, logout_button
from langchain_community.chat_message_histories import StreamlitChatMessageHistory


def main_chat(auth: dict):
    history = StreamlitChatMessageHistory()
    for message in history.messages:
        st.chat_message(message.type).write(message.content)
    question = st.chat_input("")
    if question:
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            conversation_id = st.session_state["conversation_id"] if st.session_state["conversation_id"] else ""
            inputs = {"user_subscribed": str(st.session_state.user_subscribed)}
            stream = post_chat_message(inputs, query=question, user=auth["user"]["email"], conversation_id=conversation_id)
            answer_area = st.empty()
            answer_text = ""
            for event in stream:
                if event["event"] == "message":
                    answer_text += event["answer"]
                    answer_area.write(answer_text)
                elif event["event"] == "message_end":
                    st.session_state["conversation_id"] = event["conversation_id"]
            history.add_user_message(question)
            history.add_ai_message(answer_text)
