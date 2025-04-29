#Step1: Setup UI 
import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt=st.text_area("Define your AI Agent", height=70, placeholder="Type your system prompt here")

MODEL_NAMES_GROQ = ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile"]
MODEL_NAME_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select a Provider", ["Groq", "OpenAI"])

if provider == "Groq":
    model_name = st.selectbox("Select Groq Model: ", MODEL_NAMES_GROQ)
else:
    model_name = st.selectbox("Select OpenAI Model: ", MODEL_NAME_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query: ", height=150, placeholder="Type your query here")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent"):
    if user_query.strip():            #removes blankspace
        #Step2: Connect to backend via url
        payload={
            "model_name": model_name,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")