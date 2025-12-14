# 🚀 LangGraph Website Summarizer – README

A clean and modular implementation of a **Website Summarizer App** using **LangGraph**, **async pipelines**, and **Hugging Face summarization models**. This README explains every component, directory, and the project flow so you can understand, extend, and present it easily.

---

# 📌 Overview

This project fetches any website URL, extracts readable content, splits it into chunks, summarizes all chunks using a transformer model, and returns a clean final summary.

It is structured into **4 main layers**:

1. **steps/** → Small reusable processing functions
2. **agent/** → Orchestrates steps using LangGraph-like logic
3. **ui/** → Streamlit frontend for user interaction
4. **main.py** → CLI runner (Optional)

---

# 📂 Project Structure

```
langgraph-website-summarizer/
│
├── steps/
│   ├── fetcher.py
│   ├── parser.py
│   ├── splitter.py
│   ├── summarizer.py
│
├── agent/
│   ├── summarizer_agent.py
│   ├── graph.py
│
├── ui/
│   ├── app.py
│
├── README.md
└── main.py
```

---

# 🧩 Components — Explained

Below is a **simple, clear explanation** of every file.

---

# 📁 steps/fetcher.py

"Fetches the raw HTML for a URL"

**Why we use it?**
We need a dedicated async function to fetch pages reliably.

**Key functions:**

* `fetch_url(url)` → downloads the webpage using `aiohttp`

**Reason:** Separation of concerns — fetching should not mix with parsing.

---

# 📁 steps/parser.py

"Extracts clean text from HTML using BeautifulSoup."

**Why?**
Websites contain scripts, ads, styles — this removes all unnecessary content.

**Key function:**

* `extract_main_text(html)`

---

# 📁 steps/splitter.py

"Splits long text into chunks for summarization."

**Why?**
Models like BART have a token limit (~1024 tokens), so text must be chunked.

**What it does:**

* Uses HuggingFace tokenizer
* Splits tokens into safe ranges (350/token chunk)

---

# 📁 steps/summarizer.py

"Runs the HuggingFace summarization model."

**Why?**
One chunk → one summary → combine → final summary

**Key points:**

* Uses BART-large-CNN
* Summarizes each chunk
* Returns a merged readable summary

---

# 📁 agent/summarizer_agent.py

"Orchestrates all steps like a workflow."

**This file is the brain of the entire system.**

### Steps it performs:

1. Fetch URL
2. Extract text
3. Split into chunks
4. Summarize chunks
5. Build response JSON

**Why separate agent?**

* Clean architecture
* Easy to replace steps
* Easy to create LangGraph workflows later

---

# 📁 agent/graph.py

"Optional LangGraph-style Node + Graph classes."

This gives structure similar to LangGraph pipelines:

* Nodes
* Dependency chains
* Execution order

**Purpose:** makes the system modular and visually representable.

---

# 📁 ui/app.py

Streamlit UI for entering URLs.

**Features:**

* Input URL
* Button to summarize
* Show number of chunks
* Display clean summary

**Why Streamlit?**

* Simple UI
* No frontend coding
* Runs locally

Run using:

```
streamlit run ui/app.py
```

---

# 📁 main.py

Simple CLI runner to test backend logic without UI.

Usage:

```
python main.py https://example.com
```

---

# ▶️ How the Pipeline Works

```
URL → fetcher → parser → splitter → summarizer → final summary
```

### Example Flow

1. Enter URL in Streamlit
2. Backend fetches HTML
3. Parser extracts readable text
4. Splitter creates safe-size chunks
5. Summarizer processes each chunk
6. UI displays:

   * total chunks
   * final summary

---

# 🔧 Setup Instructions

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run UI

```
streamlit run ui/app.py
```

### 3️⃣ Test backend

```
python main.py https://example.com
```

---

# ⭐ Advantages of This Architecture

✔ Clean separation of concerns
✔ Easy to debug each step
✔ Reusable modules
✔ Simple UI for testing
✔ Can be extended to full LangGraph workflows

---

# 📌 Future Improvements

* Add async parallel summarization
* Add LangGraph visualization of nodes
* Add keyword extraction
* Add embeddings + vector store

---

# 🎉 Conclusion

This project is a clean and modular starter template for website summarization using LangGraph-style architecture. Perfect for learning, demos, and real-world usage.


