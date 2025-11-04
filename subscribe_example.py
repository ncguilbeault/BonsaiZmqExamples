import argparse
import zmq
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, default="", help="Topic to subscribe to")
    parser.add_argument("--connect", type=str, default="tcp://localhost:5557", help="ZeroMQ connection string")
    args = parser.parse_args()

    topic = args.topic
    connect = args.connect

    logging.info(f"Subscribing to topic '{topic}' on '{connect}'")

    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(connect)

    while True:

        logging.info(f"Waiting for messages on topic '{topic}'...")

        socket.setsockopt_string(zmq.SUBSCRIBE, topic)
        message = socket.recv_string()

        logging.info(f"Received message: {message}")