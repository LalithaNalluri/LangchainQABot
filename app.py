from langchain.llms import OpenAI
from constants import openai_key
import os
os.environ["OPENAI_API_KEY"]=openai_key

import streamlit as st


##Function to Load OpenAI model

def get_openai_response(question):
    llm=OpenAI(temperature=0.7)
    response=llm(question)
    return response

#intialize Streamlit app
st.set_page_config(page_title="Q&A bot")
st.header("Langchain app")
input=st.text_input("Input: ",key="input")
response=get_openai_response(input)
submit=st.button("Ask question")

if submit:
    st.subheader("Response is")
    st.write(response)