import random
import time

processed_orders = set()  # simple idempotency (in-memory)

def process_order(order_id, amount):
    print(f"[INFO] Processing order {order_id}")

    # idempotency check
    if order_id in processed_orders:
        print(f"[INFO] Order {order_id} already processed")
        return "skipped"

    # simulate random failure
    if random.random() < 0.5:
        print(f"[ERROR] Order {order_id} failed")
        raise Exception("Random failure")

    # simulate processing time
    time.sleep(2)

    processed_orders.add(order_id)
    print(f"[SUCCESS] Order {order_id} processed")

    return "success"
