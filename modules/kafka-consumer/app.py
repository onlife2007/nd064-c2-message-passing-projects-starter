import json
import os

from kafka import KafkaConsumer
from app.udaconnect.services import LocationService

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER,
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('ascii')))
for message in consumer:
    value = message.value
    location = LocationService.create(value)