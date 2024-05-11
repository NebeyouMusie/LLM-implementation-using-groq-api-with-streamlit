import os
import streamlit as st
from groq_client import get_chat_completion
from config import load_config

# Load the environment variables
load_config()

user_input = st.chat_input('start typing')

if not user_input: 
    st.title('Hello there 👋')


model_choice = st.sidebar.selectbox('Choose Model', ('LLaMA3 8b', 'LLaMA3 70b', 'Mixtral 8x7b', 'Gemma 7b'))

model_map = {
    'LLaMA3 8b': 'llama3-8b-8192',
    'LLaMA3 70b': 'llama3-70b-8192',
    'Mixtral 8x7b': 'mixtral-8x7b-32768',
    'Gemma 7b': 'gemma-7b-it',
}

model = model_map.get(model_choice, 'llama3-8b-8192')

response = get_chat_completion(user_input, model)
st.write(response)
