# import logging
# import os
# from datetime import datetime

# from app.udaconnect.models import Connection, Location, Person
# from app.udaconnect.schemas import (
#     ConnectionSchema,
#     LocationSchema,
#     PersonSchema,
# )
# from app.udaconnect.services import LocationService
# from flask import request, g, Response
# from flask_accepts import accepts, responds
# from flask_restx import Namespace, Resource
# from typing import Optional, List
# from kafka import KafkaConsumer

# logger = logging.getLogger("udaconnect-kafka-consumer")

# class UdaConnectConsumer:
#     def __init__(self):
#         # do nothing

#     def consume(self):
#         TOPIC_NAME = os.environ["TOPIC_NAME"]
#         KAFKA_SERVER = os.environ["KAFKA_SERVER"]
#         logger.warning(f"TOPIC_NAME: {TOPIC_NAME}")
#         consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
#         for message in consumer:
#             logger.warning(message)
#             location = LocationService.create(message)
#             logger.warning(location)