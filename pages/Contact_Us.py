import streamlit as st

st.header('Contact Me...')

with st.form(key='email_forms'):
    email = st.text_input('Your Email')
    message = st.text_area('Your Message')
    button = st.form_submit_button('Submit')

    if button:
        print('Button is pressed')
