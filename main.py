import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2,vertical_alignment='center')

with col1:
    st.image('images/image.jpg', width=300)

with col2:
    st.title('Jeeva S')
    content = """
                Hi there! I’m Jeeva S, a passionate junior Python developer with a strong foundation in object-oriented programming. 
                I thrive on solving complex problems and turning ideas into functional code. 
                During my studies at [Your University], I honed my skills in Python, web frameworks, and data analysis."""
    st.info(content)

content_1 = 'Below you can find some of the apps I have built in python, Feel free to contact me...'
st.write(content_1)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

data_frame = pandas.read_csv('data.csv',sep=';')

with col3:
    for index, row in data_frame[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source code]({row["url"]})')

with col4:
    for index, row in data_frame[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source code]({row["url"]})')