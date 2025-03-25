from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.vllm_client import query_vllm

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins during development (adjust in production!)
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    # Parse JSON body from frontend
    data = await request.json()
    user_message = data.get("message", "")

    # Forward message to vLLM and get generated response
    response_text = await query_vllm(user_message)

    # Return response back to frontend
    return {"response": response_text}