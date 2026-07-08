import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    "video_pipeline"
)

print()

print("Documents :", collection.count())

print()