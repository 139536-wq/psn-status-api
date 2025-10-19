from fastapi import FastAPI
import random

app = FastAPI()  # <- this line is required

STATUSES = [
    "All PlayStation servers are online.",
    "PlayStation Store is under maintenance.",
    "PSN login services are unstable.",
    "Online multiplayer services are temporarily down.",
    "Everything is running smoothly."
]

@app.get("/status")
def get_status():
    return {"status": random.choice(STATUSES)}
