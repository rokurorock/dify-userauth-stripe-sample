from dotenv import load_dotenv

load_dotenv(override=True)

import streamlit as st
from streamlit_supabase_auth import login_form, logout_button
from chat import main_chat
from stripe_auth import is_active_subscriber, stripe_payment_button


APP_NAME = "myapp"


def main() -> None:
    st.header(APP_NAME)
    # login auth
    auth = login_form(providers=["google"])
    if not auth:
        return
    if "conversation_id" not in st.session_state:
        st.session_state.conversation_id = None
    # dify chat
    main_chat(auth)
    with st.sidebar:
        user_email = auth["user"]["email"]
        st.write(f"Welcome {user_email}")
        # logout
        logout_button()
        # stripe
        is_subscriber = user_email and is_active_subscriber(user_email)
        if not is_subscriber:
            stripe_payment_button(text="Subscribe now!", customer_email=user_email)
            st.session_state.user_subscribed = False
            st.stop()
        elif is_subscriber:
            st.session_state.user_subscribed = True


if __name__ == "__main__":
    main()
