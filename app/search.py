import requests
from app.embed import get_embedding

ENDEE_URL = "http://localhost:8000"
INDEX_NAME = "documents"

def search(query: str):
    response = requests.post(
        f"{ENDEE_URL}/api/v1/query",
        json={
            "index": INDEX_NAME,
            "vector": get_embedding(query),
            "top_k": 2
        }
    )
    print("Status:", response.status_code)
    print("Raw response:")
    print(response.text)
    return response.text


if __name__ == "__main__":
    result = search("What is semantic search?")
    print(result)
