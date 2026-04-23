from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

def ask_model(prompt: str) -> str:
    payload ={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False 
    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=60)
    r.raise_for_status()
    return r.json().get("response","").strip()

@app.get("/finance-check/{customer_id}")
def finance_check(customer_id:str):

    r= requests.get(
        f"http://mock-core-api:8001/customer/{customer_id}"
    )

    customer = r.json()
    print("DEBUG customer:", customer)

    if not isinstance(customer,dict) or "name" not in customer:
        return{
            "error": "Customer not found or invalid response",
            "raw_response": customer
        }
    
    prompt = f"""
    You are a cautious banking assistant.
    Given the data below , decide of financing should be Approved or Rejected.

    Customer:
    - Name: {customer["name"]}
    - Balance: {customer["balance"]}
    - Eligible fag: {customer["eligible_financing"]}

    Rules:
    - If eligible flag is tue and balance >= 10000 -> Approved
    - Otherwise -> Rejected

    Answer with only one word: Approved or Rejected
    """
    ai_decision = ask_model(prompt)
    
    return {
       "customer": customer["name"],
       "balance": customer["balance"],
       "ai_decision": ai_decision
    }