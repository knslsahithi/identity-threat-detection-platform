import json
import os

LOG_FILE = "logs/identity_events.json"


def save_event(event):

    os.makedirs("logs", exist_ok=True)

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as file:
            try:
                events = json.load(file)
            except json.JSONDecodeError:
                events = []

    else:
        events = []

    events.append(event)

    with open(LOG_FILE, "w") as file:
        json.dump(events, file, indent=4)