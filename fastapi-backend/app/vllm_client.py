import httpx

# URL of vLLM server (replace later with actual service IP/hostname)
VLLM_ENDPOINT = "http://vllm-service:8000/generate"

# Function to send prompt to vLLM server
async def query_vllm(prompt: str) -> str:
    # --- MOCKED RESPONSE FOR NOW ---
    # Just echoing back user message.
    # Later, we'll make an actual HTTP call to vLLM server.
    return f"Echo: {prompt}"

    # --- REAL vLLM CALL (Uncomment & adjust later) ---
    # async with httpx.AsyncClient() as client:
    #     response = await client.post(VLLM_ENDPOINT, json={"prompt": prompt})
    #     result = response.json()
    #     return result.get("text", "")