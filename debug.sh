#!/bin/bash
PYTHON3=/usr/bin/python3.7/bin/python3
export FLASK_APP=./app/app.py
export FLASK_DEBUG=1
export VERIFICATION_TOKEN=***DUMMY***
export SLACK_API_TOKEN=***DUMMY****
export LOG_FOLDER=/var/log/kratos-web
export FLASK_ENV=development

#./mkdir_log.sh
$PYTHON3 -m flask run --host=0.0.0.0
