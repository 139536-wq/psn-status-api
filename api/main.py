from fastapi import FastAPI
import random

app = FastAPI()  # Vercel looks for this

STATUSES = [
    "All PlayStation servers are online and running smoothly.",
    "PlayStation Store is under maintenance for updates.",
    "PSN login services are currently unstable.",
    "Online multiplayer services are temporarily down.",
    "Some services are experiencing minor delays, but most features are functional.",
    "Maintenance is ongoing. Certain games or services may not be available."
]

@app.get("/status")
def get_status():
    return {"status": random.choice(STATUSES)}
