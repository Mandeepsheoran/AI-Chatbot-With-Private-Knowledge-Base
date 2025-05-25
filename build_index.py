from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
import config

def build_index():
    documents = SimpleDirectoryReader(config.KNOWLEDGE_DIR).load_data()
    embed_model = OllamaEmbedding(model_name=config.EMBED_MODEL)
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
    index.storage_context.persist()
    print("✅ Index built and saved.")

if __name__ == "__main__":
    build_index()
