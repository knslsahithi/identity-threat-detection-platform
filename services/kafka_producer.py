import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def publish_event(event):

    producer.send(
        "identity-events",
        value=event
    )

    producer.flush()

    print("✅ Event published to Kafka")