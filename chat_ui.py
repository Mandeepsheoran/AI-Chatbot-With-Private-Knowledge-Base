# chat_ui.py
import streamlit as st
from query_engine import get_query_engine

st.set_page_config(page_title="Private RAG Chatbot", layout="wide")

st.title("Carnival Testing Chatbot")
st.markdown("Ask questions based on Carnival testing knowledge base.")

# Load the query engine
query_engine = get_query_engine()

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = query_engine.query(user_input)
        st.markdown(response.response)
        st.session_state.messages.append({"role": "assistant", "content": response.response})
