import streamlit as st
from latex import fill_document
from datetime import date

from inputs import Title


st.set_page_config(
    page_title="API Documentation generator",
    page_icon="📚",
    layout="centered",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title(":green[API] Documentation generator 📚")

main_title = st.text_input("Title", "API Documentation")
author = st.text_input("Author")
date = st.date_input("Date")

title = Title(title=main_title, author=author, date=str(date))

if st.button("Generate", type="primary"):
    fill_document(title=title)
    data = open('output/docs.pdf', 'rb').read()

    st.download_button(
        label="Download PDF",
        data=data,
        file_name='docs.pdf',
        mime='application/pdf',
    )