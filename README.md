pip install fastapi uvicorn redis rq pydantic

# start redis
redis-server

# run API
uvicorn api.main:app --reload

# run worker
python worker/worker.py
``

curl -X POST http://localhost:8000/orders \
-H "Content-Type: application/json" \
-d '{"order_id":"123","amount":100}'
