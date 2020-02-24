#!/bin/bash
PYTHON3=/usr/bin/python3.7/bin/python3

sudo $PYTHON3 -m pip install virtualenv
virtualenv "flask-demo"
source flask-demo/bin/activate

$PYTHON3 -m pip install gunicorn flask
