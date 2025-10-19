import random
from fastapi import FastAPI

app = FastAPI(title="PlayStation Server Status API", version="1.0.0")

# List of possible PlayStation server status messages
STATUSES = [
    "All PlayStation services are fully operational, including PSN login, multiplayer, and the PlayStation Store.",
    "The PlayStation Store is currently undergoing maintenance. Purchases and browsing may be unavailable for some users.",
    "PSN login services are experiencing intermittent issues. Some users may have trouble signing in or staying connected.",
    "Online multiplayer functionality is temporarily unavailable. You may not be able to join or host online matches.",
    "Game updates and downloads may be slower than usual due to server congestion.",
    "Party chat and voice communication features are currently unstable in certain regions.",
    "Payment processing in the PlayStation Store is facing temporary disruptions. Try again later.",
    "Regional server issues detected. Some features may not work depending on your location.",
    "PSN is currently experiencing high traffic. You may notice performance delays.",
    "Major outage detected across multiple PlayStation services, including login, online play, and store access.",
    "Servers are restarting for scheduled maintenance. Services will resume shortly.",
    "All systems are running smoothly, and no known issues are affecting PlayStation services."
]

@app.get("/status", summary="Get current PlayStation server status")
def get_playstation_status():
    """
    Returns a random PlayStation server status.
    (Note: This is a simulated response and not an official status.)
    """
    return {"status": random.choice(STATUSES)}
