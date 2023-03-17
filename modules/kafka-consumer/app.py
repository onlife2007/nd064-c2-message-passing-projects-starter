import logging
import json
import os

from app import create_app
from kafka import KafkaConsumer
from app.udaconnect.services import LocationService

app = create_app(os.getenv("FLASK_ENV") or "test")
logger = logging.getLogger("udaconnect-kafka-consumer")

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER,
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('ascii')))
for message in consumer:
    value = message.value
    logger.warning(value)
    location = LocationService.create(value)
    logger.warning(location)