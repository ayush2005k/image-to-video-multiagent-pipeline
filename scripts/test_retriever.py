from rag.retriever import retrieve_context


query = "Corporate annual conference highlights"

results = retrieve_context(query)

print()

print("========== RETRIEVER ==========\n")

for i, doc in enumerate(results, start=1):

    print(f"Result {i}")

    print(f"ID : {doc['id']}")

    print(f"Source : {doc['source']}")

    similarity = 1 / (1 + doc["distance"])

    print(f"Similarity : {similarity:.2%}")

    print()

    print(doc["text"])

    print()

    print("-" * 50)