# vector_databases
# CHROMA DB


## 📌 Overview

This project demonstrates how to use a vector database using ChromaDB. It shows how to:

* Create a collection
* Store text documents
* Perform similarity-based queries

---

## 🛠️ Tech Stack

* Python
* ChromaDB

---

## 📂 Project Structure

```bash
.
├── query.py
├── requirements.txt
├── README.md
```

---

## ⚙️ Environment Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/vector_databases.git
cd vector_databases
```

---

### 2️⃣ Create Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install chromadb
```

OR (if using requirements.txt):

```bash
pip install -r requirements.txt
```

---

## ▶️ Execution Steps

Run the Python script:

```bash
python query.py
```

---

## 📊 What the Code Does

* Creates a ChromaDB client
* Creates a collection named **vehicles**
* Adds sample documents:

  * car
  * plane
  * boat
  * bus
* Performs a semantic search query:

  ```
  "vehicle that run on road"
  ```
* Returns the most relevant results

---

## 🧪 Example Output

```bash
Collection created: vehicles
{'ids': [...], 'documents': [...], 'distances': [...]}
```

---

## 📦 requirements.txt

```txt
chromadb
```

---

## ❗ Notes

* Do NOT upload `venv/` folder (add it to `.gitignore`)
* Ensure Python 3.8+ is installed
* Internet connection may be required for some dependencies

---

## 📌 Future Improvements

* Add embeddings visualization
* Integrate with LangChain
* Build a UI using Streamlit

---

## 👩‍💻 Author

Bhargavi
<img width="1555" height="161" alt="image" src="https://github.com/user-attachments/assets/0e3fc2c0-6d23-42c9-beac-f439dfaa0df5" />
