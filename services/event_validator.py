from models.identity_event import IdentityEvent


def validate_event(event: IdentityEvent):

    if not event.user:
        return False, "User is missing"

    if not event.timestamp:
        return False, "Timestamp is missing"

    if not event.location:
        return False, "Location is missing"

    if not event.device:
        return False, "Device is missing"

    if not event.application:
        return False, "Application is missing"

    if event.status not in ["Success", "Failure"]:
        return False, "Invalid Status"

    return True, "Event Valid"