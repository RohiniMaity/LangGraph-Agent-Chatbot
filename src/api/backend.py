#Step1: Setup Pydantic Model (Schema Validation)
from typing import List
from src.common.pydantic_models.request_model import RequestState


#Step2: Setup AI Agent from FrontEnd Request
from fastapi import FastAPI
from src.core.ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}

    # Create AI Agent and get response from it! 
    response=get_response_from_ai_agent(llm_id = request.model_name,
                                        query = request.messages,
                                        allow_search = request.allow_search,
                                        system_prompt = request.system_prompt,
                                        provider = request.model_provider)
    return response

#Step3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)