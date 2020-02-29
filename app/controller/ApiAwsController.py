from flask import request
from flask import render_template
from flask import Blueprint, request, json
from flask import Flask, request, render_template, send_from_directory, make_response, jsonify
from flask import flash, redirect, session, abort
import os
import slack
import time

from app.helper import helper
from app.config import Configuration


class ApiAwsController:
    config = Configuration.Configuration()

    def __init__(self):
        pass

    def list_ec2_tags(self, tags):
        return make_response(jsonify(
            {
                "data": [
                    {
                        "name": "devel",
                        "instance_id": "id-115654477",
                        "ami_id": "ami-56446487879",
                        "owner": "za577",
                        "cpu": "6c/2h",
                        "status": "running",
                    },
                    {
                        "name": "compilation-009.300.000",
                        "instance_id": "id-81565447a",
                        "ami_id": "ami-56446487879",
                        "owner": "rint",
                        "cpu": "6c/2h",
                        "status": "stopped",
                    },
                    {
                        "name": "compilation-009.300.001",
                        "instance_id": "id-81565447a",
                        "ami_id": "ami-56446487879",
                        "owner": "rint",
                        "cpu": "6c/2h",
                        "status": "running",
                    }
                ]
            }
        ), 200, {"content_type": "application/json"})


api_aws_controller = ApiAwsController()
