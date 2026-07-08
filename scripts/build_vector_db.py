import chromadb

from sentence_transformers import SentenceTransformer

from rag.knowledge_base import load_documents


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="video_pipeline"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = load_documents()

# Remove old documents if they exist
existing = collection.get()

if existing["ids"]:
    collection.delete(ids=existing["ids"])

for doc in documents:

    embedding = embedding_model.encode(
        doc["document"]
    ).tolist()

    collection.add(

        ids=[doc["id"]],

        documents=[doc["document"]],

        embeddings=[embedding],

        metadatas=[
            {
                "source": doc["source"]
            }
        ]
    )

print()

print("Vector Database Created")

print(f"Documents Indexed : {len(documents)}")