import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "identity-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="identity-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Waiting for identity events...\n")

for message in consumer:
    print("Identity Event Received")
    print(message.value)
    print("-" * 60)