def normalize_event(event):

    normalized_event = {
        "event_id": f"EVT-{event.user}-{event.timestamp}",
        "timestamp": event.timestamp,
        "user": event.user.lower(),
        "location": event.location.title(),
        "device": event.device,
        "application": event.application,
        "status": event.status.upper()
    }

    return normalized_event