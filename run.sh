#!/bin/bash

gunicorn --bind 0.0.0.0:5000 wsgi:app


#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
#https://medium.com/faun/deploy-flask-app-with-nginx-using-gunicorn-7fda4f50066a