import requests
from app.embed import get_embedding

ENDEE_URL = "http://localhost:8000"
INDEX_NAME = "documents"

def ingest_documents():
    with open("data/documents.txt", "r") as f:
        docs = f.readlines()

    vectors = []
    for idx, text in enumerate(docs):
        vectors.append({
            "id": str(idx),
            "values": get_embedding(text),
            "metadata": {
                "text": text.strip()
            }
        })

    payload = {
        "index": INDEX_NAME,
        "vectors": vectors
    }

    response = requests.post(
        f"{ENDEE_URL}/api/v1/vectors/upsert",
        json=payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    ingest_documents()
