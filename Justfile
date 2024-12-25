
format:
	#!/bin/sh
	source venv/bin/activate
	black . --extend-exclude="(coqui|tortoise-tts)"

run:
	python main.py
