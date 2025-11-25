# Async API Fetcher

A lightweight, fully asynchronous API fetching utility built using **aiohttp**, **asyncio**, **TaskGroup**, **tenacity retries**, and **rich logging**.

This project demonstrates:

- Concurrent HTTP requests
- Graceful error handling
- Automatic retries with exponential backoff
- Clean structured logging
- Modern Python 3.11+ features (TaskGroup)

---

## 🚀 Features

- Fetch multiple URLs concurrently using `asyncio.TaskGroup`
- Automatic retry for transient errors using `tenacity`
- Colored + structured logs using `rich`
- Simple, extensible architecture
- Works with any JSON API

---

## 📦 Installation

Make sure you have Python **3.11+**.

```bash
uv sync
```

Or manually:

```bash
uv add aiohttp tenacity rich
```

---

## 📁 Project Structure

```
async_api_fetcher/
│
├── fetcher.py
├── utils.py
├── main.py
├── pyproject.toml
└── README.md
```

---

## 🧠 How It Works

### **fetcher.py**

- Opens a single `aiohttp.ClientSession`
- Uses `asyncio.TaskGroup` to run all fetches concurrently
- Cleans failed results

### **utils.py**

- Configures Rich logging

### **main.py**

- Defines URL list
- Calls `fetch_all()`
- Prints results

---

## ▶️ Usage

Run the script:

```bash
uv run python main.py
```

Or without uv:

```bash
source .venv/bin/activate
python main.py
```

---

## 🔍 Example Output

```
20 URLs fetched successfully
```

Logs are printed with timestamps, colors, and helpful messages.

---

## 🔧 Configuration

You can update:

- Timeout
- Retry count
- Retry backoff

Modify in `fetcher.py` where tenacity is applied.

---

## 🧪 Testing URLs

Here are good test endpoints:

- `https://jsonplaceholder.typicode.com/posts/1`
- `https://httpbin.org/delay/1`
- `https://catfact.ninja/fact`

More sample URLs are included in `main.py`.

---

## 🤝 Contributing

PRs welcome! Add new features like:

- Caching
- Parallel sessions
- CLI interface

---
