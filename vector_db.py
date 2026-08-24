import chromadb


client = chromadb.PersistentClient(
    path="./chromadb"
)


collection = client.get_or_create_collection(
    name="knowledge",
)

print("向量数据库初始化完成")