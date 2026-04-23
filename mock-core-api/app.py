from fastapi import FastAPI

app = FastAPI()

customer = {
    "123": {
        "name":"Ahmed",
        "balance":50000,
        "eligible_financing":True
    }
}

@app.get("/customer/{customer_id}")
def get_customer(customer_id: str):
    return customer.get(
        customer_id,
        {"error":"Customer not found"}
    )