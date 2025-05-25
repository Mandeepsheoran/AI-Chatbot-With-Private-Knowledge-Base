
# ✅ new (works with latest LlamaIndex)
from llama_index.core import StorageContext, load_index_from_storage

from llama_index.llms.ollama import Ollama
from llama_index.core.query_engine import RetrieverQueryEngine  # ✅

import config
import os
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.settings import Settings


llm = Ollama(model="tinyllama")
embed_model = OllamaEmbedding(model_name="nomic-embed-text")
# Tell LlamaIndex to use these globally
Settings.llm = llm
Settings.embed_model = embed_model

def get_query_engine():
    if not os.path.exists("storage"):  # Ensure index is built
        raise Exception("Index not found. Run build_index.py first.")

    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context)

    
    query_engine = index.as_query_engine(llm=llm)
    return query_engine