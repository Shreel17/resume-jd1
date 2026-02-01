import chromadb

chroma_client = chromadb.Client()

def get_collection(name: str):
    return chroma_client.get_or_create_collection(name)

def delete_collection(name: str):
    try:
        chroma_client.delete_collection(name)
    except Exception:
        pass
