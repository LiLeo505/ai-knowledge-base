from config import API_KEY

from loader import load_documents
from chunker import split_text
from embedding import get_embedding
import vector_db

#入库

documents = load_documents("knowledge")

id = 0

collection = vector_db.get_collection()

for document in documents:
    chunks = split_text(document["content"])
    for chunk in chunks:
        embedding = get_embedding(chunk)
        id += 1
        collection.add(
            ids=[f"{document['filename']}_{id}"],
            documents=[chunk],
            embeddings=embedding,
            metadatas=[{"source": document["filename"]}]
        )



print("知识库构建完成")


        