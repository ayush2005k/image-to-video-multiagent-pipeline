import chromadb

from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    "video_pipeline"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_context(query: str, k: int = 2):

    embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(

        query_embeddings=[embedding],

        n_results=k

    )

    documents = []

    ids = results["ids"][0]

    texts = results["documents"][0]

    metadata = results["metadatas"][0]

    distances = results["distances"][0]

    for doc_id, text, meta, score in zip(
        ids,
        texts,
        metadata,
        distances
    ):

        documents.append(

            {
                "id": doc_id,
                "text": text,
                "source": meta["source"],
                "distance": score
            }

        )

    return documents