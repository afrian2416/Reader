import streamlit as st
import fitz  # PyMuPDF
from ebooklib import epub
from bs4 import BeautifulSoup

def read_pdf(file):
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def read_epub(file):
    book = epub.read_epub(file)
    text = ""
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            text += soup.get_text()
    return text

st.title("PDF and EPUB Reader")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "epub"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        st.write("Reading PDF file...")
        pdf_text = read_pdf(uploaded_file)
        st.text_area("PDF Content", pdf_text, height=400)
    elif file_extension == 'epub':
        st.write("Reading EPUB file...")
        epub_text = read_epub(uploaded_file)
        st.text_area("EPUB Content", epub_text, height=400)
    else:
        st.error("Unsupported file type. Please upload a PDF or EPUB file.")
