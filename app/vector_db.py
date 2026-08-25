import chromadb
from embedding import get_embedding


def get_collection():
    client = chromadb.PersistentClient(path="./chromadb")

    collection = client.get_or_create_collection(name="knowledge")

    return collection

def add_document_to_collection(document):
    collection = get_collection()
    embedding = get_embedding(document["content"])
    collection.add(
        ids=[document["filename"]],
        documents=[document["content"]],
        embeddings=embedding,
        metadatas=[{"source": document["filename"]}]
    )


def search(question,n_results=3):
    collection = get_collection()
    results = collection.query(
        query_embeddings=[get_embedding(question)],
        n_results=n_results,
    )
    return results 

