# LangGraph Agent Chatbot 🤖

A Streamlit + FastAPI-based AI chatbot UI that allows users to create and interact with powerful LLM agents powered by **Groq** and **OpenAI**. Includes optional real-time web search capability via Tavily.

---

## 🚀 Features

- 🔧 Define your **custom system prompt**
- 🧠 Choose from **Groq** or **OpenAI** models:
  - Groq: `llama3-8b-8192`, `llama3-70b-8192`, `mixtral-8x7b-32768`, `llama-3.3-70b-versatile`
  - OpenAI: `gpt-4o-mini`
- 🌐 Enable optional **web search** via [Tavily](https://www.tavily.com/)
- 📬 Communicates between a **Streamlit frontend** and a **FastAPI backend**
- 📡 Simple and interactive UI with support for persistent conversations

---

## 🗂️ Project Structure

```
LangGraph-Agent-Chatbot/
│
├── src
├── ├── core
├── ├── ├── ai_agent.py           # Core logic to create agents and fetch responses
├── ├── UI
├── ├── ├── frontend.py           # Streamlit UI for interacting with the chatbot
├── ├── APIs
├── ├── ├── backend.py            # FastAPI backend that handles chat requests
├── ├── common
├── ├── ├── pydantic_models
├── ├── ├── ├── request_model.py  # Pydantic Model for Request 
├── ├── .env                      # API keys for Groq, OpenAI, and Tavily
├── ├── requirements.txt          # List of required Python packages
├── └── README.md                 # You're here!
```

---

## 🔑 Prerequisites

- Python 3.8+
- API Keys for:
  - [Groq API](https://console.groq.com/)
  - [OpenAI API](https://platform.openai.com/)
  - [Tavily API](https://www.tavily.com/)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/LangGraph-Agent-Chatbot.git
cd LangGraph-Agent-Chatbot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Setup `.env` file**

Create a `.env` file in the root directory and add your API keys:

```dotenv
GROQ_API_KEY=your-groq-api-key
OPENAI_API_KEY=your-openai-api-key
TAVILY_API_KEY=your-tavily-api-key
```

---

## 🛠️ Running the Application

### Step 1: Start the FastAPI backend

```bash
python backend.py
```

Visit: `http://127.0.0.1:9999/docs` to explore the API in Swagger UI.

### Step 2: Start the Streamlit frontend

```bash
streamlit run frontend.py
```

Visit: `http://localhost:8501` to use the chatbot UI.

---

## 📸 Screenshots

![](/ss.png)

---

## 🧪 Example Prompts

- System Prompt:  
  `"You are a helpful AI assistant who answers concisely."`
- Query:  
  `"Summarize the benefits of using Retrieval-Augmented Generation for chatbots."`

---

## 📌 To Do

- [ ] Add support for chat history and threading
- [ ] Implement feedback mechanism (thumbs up/down)
- [ ] Deploy using Docker / Streamlit Sharing
- [ ] PDF upload support for retrieval-based QA

---

## 🙌 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Tavily Search API](https://www.tavily.com/)
- [Groq Cloud](https://console.groq.com/)

---

## 📄 License

MIT License

---

## 💬 Questions?

Feel free to open an [issue](https://github.com/yourusername/LangGraph-Agent-Chatbot/issues) or contact the maintainer.
