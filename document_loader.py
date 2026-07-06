import os
import tempfile
from pathlib import Path
from typing import Optional,List
from langchain_community.document_loaders import TextLoader,PyPDFLoader

from dotenv import load_dotenv
load_dotenv()


#text loader

# def load_text_file(a):
#     loader = TextLoader(a)
#     docs = loader.load()
#     print(docs[0].page_content)


# load_text_file("g.txt")


#PDF loader

def pdfLoader(a:str):
    loader = PyPDFLoader(a)
    docs = loader.load()
    for doc in docs:
       #print 
        print(doc.page_content)

