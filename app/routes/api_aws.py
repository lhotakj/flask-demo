#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint

from app.controller.ApiAwsController import api_aws_controller

api_aws = Blueprint("api_aws", __name__)


@api_aws.route('/api/ec2/tags/<string:tags>', methods=['GET'])
def list_ec2_tags(tags):
    return api_aws_controller.list_ec2_tags(tags)


@api_aws.route('/api/ec2/action/<string:action>', methods=['POST'])
def action_ec2(action):
    return api_aws_controller.action_ec2(action)
