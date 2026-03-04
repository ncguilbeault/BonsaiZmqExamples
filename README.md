# BonsaiZmqExamples

These are simple examples for how to use ZeroMQ to share data between Bonsai and Python.

## Dependencies

1. **Install [uv](https://github.com/astral-sh/uv):**
	If you don't have `uv` installed, follow instructions at https://github.com/astral-sh/uv or run:
	```bash
	pip install uv
	```

2. **Install [Bonsai](https://bonsai-rx.org/docs/articles/installation.html):**
	Follow the instructions in the article to download and install Bonsai.

3. **Clone the [repo](https://github.com/ncguilbeault/BonsaiZmqExamples.git):**
	With [Git](https://git-scm.com/install/) installed, clone the repo and change to the directory.
	```bash
	git clone https://github.com/ncguilbeault/BonsaiZmqExamples.git
	cd BonsaiZmqExamples
	```

## Sending Data from Bonsai to Python

1. **Start Bonsai and open the PublishExample workflow:**
	Run the workflow to open the socket and start publishing messages.

2. **Run the Python script:**
	Run the python script with:
	```bash
	uv run subscribe_example.py
	```

## Expected Output

Once both the Python script and Bonsai workflow are running, you should start to see messages being printed in the Python terminal.

## Sending a multipart message from Python into Bonsai

1. **Run the Python script:**
	To start sending messages to Bonsai, start the Python script with:
	```bash
	uv run publish_multipart_msg.py
	```

2. **Start the Bonsai workflow:**
	Open the SubscribeMultipart workflow in Bonsai and run.

## Expected Output
When you start the Python script, you should start to see messages printed to the console that show the message header, as well as the message payload. In Bonsai, you should see that the `ParseHeader` operator will display the message header and the `ParseData` operator will display the payload converted to an integer.
