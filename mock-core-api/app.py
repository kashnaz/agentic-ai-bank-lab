from fastapi import FastAPI

app = FastAPI()

customers = {
    "123": {
        "name":"Ahmed",
        "balance":50000,
        "eligible_financing":True
    }
}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    return customers.get(
        customer_id,
        {"error":"Customer not found"}
    )