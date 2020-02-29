#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from app.controller.ApiSlackController import api_slack_controller

api_slack = Blueprint("api_slack", __name__)


@api_slack.route('/api/slack/event', methods=['POST', 'GET'])
def slack_event():
    return api_slack_controller.slack_event()


@api_slack.route('/api/slack/command/<string:command>', methods=['POST', 'GET'])
def slack_command(command):
    return api_slack_controller.slack_command(command)
