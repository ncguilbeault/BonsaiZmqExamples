# BonsaiZmqExamples

This is a minimal example for using ZeroMQ to publish messages from Bonsai and subscribing to them using Python and `pyzmq`.

## Setup with uv

1. **Install [uv](https://github.com/astral-sh/uv):**
	If you don't have `uv` installed, follow instructions at https://github.com/astral-sh/uv or run:
	```bash
	pip install uv
	```

2. **Run the example:**
	In this folder, run:
	```bash
	uv run subscribe_example.py
	```

## Setup with Bonsai

1. **With Bonsai 2.9 installed:**
	From the command line, run `bonsai --no-editor` to bootstrap the environment. Then, open `PublishExample.bonsai` and start.

## Expected Output

Once both the Python script and Bonsai workflow are running, you should start to see messages being printed in the Python terminal.
