import streamlit as st
from latex import fill_document


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

st.title("API Documentation generator")

if st.button("Generate", type="primary"):
    fill_document()
    data = open('output/docs.pdf', 'rb').read()

    st.download_button(
        label="Download data as CSV",
        data=data,
        file_name='docs.pdf',
        mime='application/pdf',
    )