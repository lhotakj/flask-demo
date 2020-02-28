#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from app.controller.ApiController import api_controller

api = Blueprint("api", __name__)


@api.route('/api/slack/event', methods=['POST', 'GET'])
def slack_event():
    return api_controller.slack_event()


@api.route('/api/slack/command/<string:command>', methods=['POST', 'GET'])
def slack_command(command):
    return api_controller.slack_command(command)
