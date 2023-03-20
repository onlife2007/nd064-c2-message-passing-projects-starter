import logging
import os
from datetime import datetime, timedelta
from typing import Dict, List

from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import grpc
import person_pb2
import person_pb2_grpc

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

url = URL.create(
            drivername="postgresql",
            username=DB_USERNAME,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
engine = create_engine(url)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

class PersonService(person_pb2_grpc.PersonServiceServicer):
    def RetrieveAll(self, request, context):
        persons = session.query(Person).all()
        result = person_pb2.PersonMessageList()
        for person in persons:
            person_grpc = person_pb2.PersonMessage(
                id= person.id,
                first_name= person.first_name,
                last_name= person.last_name,
                company_name= person.company_name
            )
            result.persons.append(person_grpc)
        
        return result
