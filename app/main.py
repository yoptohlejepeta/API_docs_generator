import streamlit as st
from doc_gen import fill_document
from datetime import date

from inputs import Title
from utils import read_markdown_file

about = read_markdown_file("README.md")
center_title = "<style>h1{text-align: center; font-size: 50px;}</style>"

st.set_page_config(
    page_title="API Documentation generator",
    page_icon="📜",
    layout="centered",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": about,
    },
)
st.markdown(center_title, unsafe_allow_html=True)

st.title("<:green[API]/> DocGen", anchor=False)

st.header("Title")

main_title = st.text_input("Title", "API Documentation")
author = st.text_input("Author")
date = st.date_input("Date")

title = Title(title=main_title, author=author, date=str(date))

if st.button("Generate", type="primary"):
    fill_document(title)
    data = open("output/docs.pdf", "rb").read()

    st.download_button(
        label="Download PDF",
        data=data,
        file_name="docs.pdf",
        mime="application/pdf",
    )
