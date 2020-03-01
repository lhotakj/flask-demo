#!/bin/bash

export FLASK_APP=./app/app.py
export FLASK_DEBUG=1
export VERIFICATION_TOKEN=***DUMMY***
export SLACK_API_TOKEN=***DUMMY****

echo "Running GUNICORN ..."
gunicorn --bind 0.0.0.0:5000 app.app:app

#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
#https://medium.com/faun/deploy-flask-app-with-nginx-using-gunicorn-7fda4f50066a
