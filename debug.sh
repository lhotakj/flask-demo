#!/bin/bash
PYTHON3=/usr/bin/python3.7/bin/python3

export FLASK_APP=./server.py
export FLASK_DEBUG=1
export VERIFICATION_TOKEN=***DUMMY***
export SLACK_API_TOKEN=***DUMMY****
$PYTHON3 -m flask run --host=0.0.0.0
