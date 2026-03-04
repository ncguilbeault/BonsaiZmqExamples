import argparse
import zmq
import logging
import time

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--connection", type=str, default="tcp://localhost:5557", help="ZeroMQ connection string")
    args = parser.parse_args()

    connection = args.connection

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(connection)

    i = 0

    while True:
        metadata = {"number": i}
        payload = i.to_bytes(4, byteorder="little")
        print(f"Metadata: {metadata}, Payload: {payload}")
        socket.send_json(metadata, flags=zmq.SNDMORE)
        socket.send(payload)
        time.sleep(1)
        i += 1
