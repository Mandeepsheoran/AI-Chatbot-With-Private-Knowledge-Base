# AI-Chatbot-With-Private-Testing -Knowledge-Base
AI-powered chatbot for querying private knowledge base of testing artifacts using LLaMA, LangChain, LlamaIndex, FAISS, comic-embed-text, and Streamlit.

Technologies Used

- Ollama:
  Provides the LLM (tinyllama) for generating embeddings and responses.

- LlamaIndex:
  Handles document indexing and querying.

- FAISS:
  A vector database for efficient similarity search.

- Nomic-Embed-Text:
  Converts text into vector embeddings for retrieval.

- Streamlit:
  A Python-based framework for building the chatbot UI.

---

Setup and Usage

1. Clone the Repository
2. Install Dependencies :- pip install -r requirements.txt
3. Start the LLM Server :- ollama serve --model tinyllama
4. Build the Knowledge Base Index:- Place your documents in the my-knowledge/ directory and run: python build_index.py
5. Launch the Chatbot :- streamlit run chat_ui.py

How It Works

Indexing:

The build_index.py script reads documents from the my-knowledge/ directory.
Text is converted into vector embeddings using the nomic-embed-text model.
The embeddings are stored in a vector database for efficient retrieval.

