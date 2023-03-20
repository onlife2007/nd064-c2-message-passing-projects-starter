import json
import logging
from concurrent import futures
import grpc
import person_pb2
import person_pb2_grpc
from app.udaconnect.services import PersonService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-person-grpc")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    person_pb2_grpc.add_PersonServiceServicer_to_server(
        PersonService(), server
    )
    logger.info("Server starting on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()