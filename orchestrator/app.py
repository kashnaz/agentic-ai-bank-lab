from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("finance-check/{customer_id}")
def finance_check(customer_id:str):

    r= requests.get(
        f"http://mock-core-api:8001/customer/{customer_id}"
    )

    customer = r.json()

    if "error" in customer:
        return customer
    
    return {
       "customer": customer["name"],
       "balance": customer["balance"],
       "financing_decision":"Approved" 
    }