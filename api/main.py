from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from queue.queue_config import queue
from tasks.tasks import process_order
from rq import Retry

app = FastAPI()

class Order(BaseModel):
    order_id: str
    amount: float

@app.post("/orders")
def create_order(order: Order):
    # simple validation
    if order.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    # push to queue
    job = queue.enqueue(
        process_order,
        order.order_id,
        order.amount,
        retry=Retry(max=3, interval=[10, 30, 60])
    )

    return {
        "message": "Order received",
        "job_id": job.id
    }