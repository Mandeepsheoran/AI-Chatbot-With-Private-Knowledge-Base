# chat_ui.py
import streamlit as st
from query_engine import get_query_engine

st.set_page_config(page_title="CUK AI Chatbot", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=80)

    st.markdown("##  Carnival Chatbot")
    st.markdown("Ask anything from your CUK testing knowledge base")

    st.markdown("---")

    # Example prompts
    st.markdown("### 💡 Try asking:")
    if st.button("🔍 What are our accessibility testing standards?"):
        st.session_state.pre_fill = "What are our accessibility testing standards?"
    if st.button("🧪 Key test cases for checkout flow"):
        st.session_state.pre_fill = "Show key test cases for checkout flow"
    if st.button("📈 Performance test patterns"):
        st.session_state.pre_fill = "Give me performance test anomalies and patterns"

    st.markdown("---")

    # Expandable explanation
    with st.expander("ℹ️ How This Works"):
        st.markdown("""
        This AI chatbot is built using:
        - 🦙 LLaMA for local inference
        - 🔗 LangChain for chaining logic
        - 📄 LlamaIndex for document context
        - 🧠 FAISS + comic-embed-text for semantic search
        - 🌐 Streamlit for UI

        **Use Case**: Answer internal QA, test case, and performance questions without manual searching.
        """)

# --- Title Banner ---
st.markdown(
    """
    <div style="background-color:#003566;padding:1rem;border-radius:8px">
        <h2 style="color:white;text-align:center;"> Carnival Testing Chatbot</h2>
        <p style="color:#d3d3d3;text-align:center;">Powered by your private Testing knowledge base</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### 💬 Start chatting below")

# Load the query engine
query_engine = get_query_engine()

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "user":
            st.markdown(f"🧑‍💻: {msg['content']}")
        else:
            st.markdown(f"🤖: {msg['content']}")

# Input from user (support prefill from sidebar buttons)
user_input = st.chat_input("Ask me anything about CUK testing...")

if user_input is None and "pre_fill" in st.session_state:
    user_input = st.session_state.pop("pre_fill")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(f"🧑‍💻: {user_input}")

    with st.chat_message("assistant"):
        response = query_engine.query(user_input)
        st.markdown(f"🤖: {response.response}")
        st.session_state.messages.append({"role": "assistant", "content": response.response})
