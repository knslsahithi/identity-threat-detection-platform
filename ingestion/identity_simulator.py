import random
from datetime import datetime
from models.identity_event import IdentityEvent
from services.event_validator import validate_event
from services.event_normalizer import normalize_event
from services.event_logger import save_event
from services.kafka_producer import publish_event

users = [
    "john.doe",
    "alice.smith",
    "michael.jones",
    "sarah.wilson",
    "admin.user"
]

locations = [
    "India",
    "USA",
    "Germany",
    "Singapore",
    "Australia"
]

devices = [
    "Windows Laptop",
    "MacBook",
    "Android Phone",
    "iPhone"
]

applications = [
    "Office365",
    "Salesforce",
    "AWS Console",
    "GitHub",
    "VPN"
]

status = [
    "Success",
    "Failure"
]


def generate_event():

    event = IdentityEvent(
        timestamp=datetime.now().isoformat(),
        user=random.choice(users),
        location=random.choice(locations),
        device=random.choice(devices),
        application=random.choice(applications),
        status=random.choice(status)
    )

    return event


if __name__ == "__main__":

    event = generate_event()

    is_valid, message = validate_event(event)

    if is_valid:

        normalized_event = normalize_event(event)

        save_event(normalized_event)

        publish_event(normalized_event)
        
        print("\nGenerated Event")
        print(event.model_dump())

        print("\nNormalized Event")
        print(normalized_event)

        print("\nValidation Status:", message)

        print("\nEvent saved successfully.")

    else:
        print(message)