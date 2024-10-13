import streamlit as st
from send_mails import send_mail

st.header('Contact Me...')

with st.form(key='email_forms'):
    name = st.text_input('your name')
    email = st.text_input('Your Email')
    raw_message = st.text_area('Your Message')
    message = f"""\
Subject: New mail from {name}

From: {email}\n
{raw_message}
    """
    button = st.form_submit_button('Submit')
    if button:
        send_mail(message=message)
        st.info('Your email sent successfully..!')