from rq import Worker
from queue.queue_config import redis_conn

if __name__ == "__main__":
    worker = Worker(["orders"], connection=redis_conn)
    worker.work()