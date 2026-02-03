#  Endee Semantic Search System

##  Project Overview

This project demonstrates a semantic search system built using Endee as the vector database.  
The system enables meaning-based retrieval by embedding user queries into vectors and retrieving the most semantically similar results using vector similarity search.

The design follows real-world production practices, where:
- vector ingestion is handled via offline pipelines, and
- the online system focuses on fast, reliable vector search.

---

##  Problem Statement

Traditional keyword-based search fails to understand semantic meaning, often returning irrelevant results.

This project solves that problem by:
- converting text into vector embeddings,
- storing and indexing them in a vector database (Endee), and
- retrieving results based on semantic similarity rather than exact keyword matches.

---

##  Use Case

- Semantic document search
- Knowledge retrieval systems
- Foundation for RAG (Retrieval Augmented Generation)
- AI-powered assistants and recommendation engines

##  System Architecture

### High-Level Flow

```text
User Query
   ↓
Embedding Model (Sentence Transformers – PyTorch)
   ↓
Endee Vector Database (Similarity Search)
   ↓
Top-K Semantically Similar Results
```

---

### 🔑 Key Design Choice

The system separates offline ingestion from online querying, which mirrors how vector databases are used in production environments.

---

##  How Endee Is Used

- Endee runs locally as a high-performance vector search engine using Docker
- The project interacts with Endee via its public query API
- Endee is responsible for:
  - vector indexing (pre-ingested data)
  - similarity search (cosine distance)
  - efficient retrieval at query time

---

##  Vector Ingestion Strategy (Important)

In real-world AI systems, vector ingestion is typically handled via offline ETL pipelines, batch jobs, or internal services — not through public query APIs.

In this project:
- Vectors are assumed to be pre-indexed in Endee
- The focus is on online semantic search
- This aligns with the design of the Endee OSS API surface

This separation improves:
- system reliability
- query latency
- security and scalability

---

##  Tech Stack

- **Vector Database:** Endee (Open Source, Docker-based)
- **Embedding Model:** Sentence Transformers (all-MiniLM-L6-v2, PyTorch backend)
- **Programming Language:** Python
- **Containerization:** Docker & Docker Compose
- **API Communication:** REST

---

##  Setup Instructions

### 1️⃣ Run Endee Locally
```bash
cd endee
docker compose up -d
```

Verify Endee is running:
```
http://localhost:8000/api/v1/health
```

Expected response:
```json
{"status":"ok"}
```

---

### 2️⃣ Install Python Dependencies
```bash
python -m pip install -r requirements.txt
```

---

### 3️⃣ Run Semantic Search
```bash
py -m app.search
```

The script:
- embeds the query at runtime
- sends it to Endee’s query API
- prints the raw response returned by Endee

---

##  Project Structure

```text
endee-semantic-search/
│
├── app/
│   ├── embed.py        # Embedding logic (PyTorch-based)
│   ├── search.py       # Semantic search via Endee API
│
├── data/
│   └── documents.txt   # Sample reference documents
│
├── endee/              # Endee OSS (Dockerized)
├── requirements.txt
├── .gitignore
└── README.md
```

---

##  Current Limitations

- Vector ingestion is not exposed via public OSS APIs
- Responses from Endee query API may be plain text (non-JSON)
- Search output is printed directly for transparency

These limitations are handled intentionally and transparently, reflecting realistic OSS usage.

---

##  Future Enhancements

- Add LLM integration to implement full RAG
- Build a dedicated ingestion pipeline
- Add a web-based UI for querying
- Support document chunking and metadata filtering
- Deploy Endee in a cloud environment

---

##  Conclusion

This project demonstrates how Endee can be used as a production-style vector search engine within an AI system.  
It emphasizes correct architecture, clarity, and real-world engineering practices over shortcuts.

The result is a clean, extensible foundation for semantic search and RAG-based applications.

---

##  Author

**Ridhi**  
B.Tech Student | AI/ML Enthusiast  
Project built as part of the Endee.io evaluation assignment
