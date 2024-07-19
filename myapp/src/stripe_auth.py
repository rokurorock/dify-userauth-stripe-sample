import streamlit as st
import stripe
import urllib.parse
import os


def str_to_bool(value):
    return value.lower() in ("true", "True")


def get_api_key() -> str:
    testing_mode = str_to_bool(os.getenv("STRIPE_TEST_MODE"))
    return os.getenv("STRIPE_API_KEY_TEST") if testing_mode else os.getenv("STRIPE_API_KEY")


def stripe_payment_button(
    text: str,
    customer_email: str,
    color="#FD504D",
    payment_provider: str = "stripe",
):
    testing_mode = str_to_bool(os.getenv("STRIPE_TEST_MODE"))
    encoded_email = urllib.parse.quote(customer_email)
    if payment_provider == "stripe":
        stripe.api_key = get_api_key()
        stripe_link = os.getenv("STRIPE_LINK_TEST") if testing_mode else os.getenv("STRIPE_LINK")
        button_url = f"{stripe_link}?prefilled_email={encoded_email}"
    else:
        raise ValueError("payment_provider must be 'stripe'")

    st.sidebar.markdown(
        f"""
    <a href="{button_url}" target="_blank">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
        unsafe_allow_html=True,
    )


def is_active_subscriber(email: str) -> bool:
    stripe.api_key = get_api_key()
    customers = stripe.Customer.list(email=email)
    # st.write(customers)
    try:
        customer = customers.data[0]
    except IndexError:
        return False

    subscriptions = stripe.Subscription.list(customer=customer["id"])
    st.session_state.subscriptions = subscriptions

    return len(subscriptions) > 0
