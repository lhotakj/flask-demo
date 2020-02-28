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


# https://api.slack.com/apps/ATPCVD9JN/general?  tokens
# https://api.slack.com/apps/ATPCVD9JN/event-subscriptions? - event subs
# https://dashboard.heroku.com/apps/jarda-demo/settings


class ApiController:
    config = Configuration.Configuration()
    client = slack.WebClient(token=config.slack_token)

    def __init__(self):
        pass

    @helper.only_get_method
    def slack_event(self):
        event_data = json.loads(request.data.decode('utf-8'))
        if event_data['token'] == self.config.verification_token:
            print('authorized')
            if "challenge" in event_data:
                return make_response(event_data.get("challenge"), 200, {"content_type": "application/json"})

            # got:
            # {'token': '****', 'team_id': 'TFFAC0JNA', 'api_app_id': 'ATPCVD9JN', 'event': {'client_msg_id': 'b874556d-3bda-408f-93a8-2b3ac5a41780', 'type': 'app_mention', 'text': '<@UTQNR2V6X> deploy', 'user': 'UFFAC0K62', 'ts': '1582823443.002000', 'team': 'TFFAC0JNA', 'blocks': [{'type': 'rich_text', 'block_id': '+6La', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'user', 'user_id': 'UTQNR2V6X'}, {'type': 'text', 'text': ' deploy'}]}]}], 'channel': 'CFD67NJ64', 'event_ts': '1582823443.002000'}, 'type': 'event_callback', 'event_id': 'EvULDG0JBX', 'event_time': 1582823443, 'authed_users': ['UTQNR2V6X']}
            if "event" in event_data:
                if event_data["event"]["type"] == "app_mention":
                    # and "type" in event_data["event"] and event_data["event"]["type"] == "app_mention"
                    my_command = event_data["event"]["text"]
                    my_channel = event_data["event"]["channel"]
                    my_user = event_data["event"]["user"]
                    print("mention:" + my_command)
                    self.client.chat_postEphemeral(
                        channel=my_channel,
                        text="OK, so you wanted `" + my_command + "`? Give me a second or two",
                        user=my_user
                    )
                    print("slack_event process")
                    self.client.chat_postEphemeral(
                        channel=my_channel,
                        text="Done!",
                        user=my_user
                    )
                    print("slack_event done")
        return make_response({}, 200, {"content_type": "application/json"})

    @helper.only_get_method
    def slack_command(self, command):
        if request.form['token'] == self.config.verification_token:
            if command == "instances":
                # ImmutableMultiDict([('token', '****'), ('team_id', 'TFFAC0JNA'), ('team_domain', 'jardalhotak'), ('channel_id', 'CFD67NJ64'), ('channel_name', 'general'), ('user_id', 'UFFAC0K62'), ('user_name', 'jarda'), ('command', '/my-instances'), ('text', 'my'), ('response_url', 'https://hooks.slack.com/commands/**'), ('trigger_id', '***')])
                payload = {'text': 'What instance dude? type `/instances my` or `/instances all`'}
                if request.form['text'] == "my":
                    payload = {
                        'text': 'Hey dude, this is a list of *your* instances (@' + request.form['user_name'] + '):'}
                if request.form['text'] == "all":
                    payload = {'text': 'Hey dude, this is a list of *all* instances:'}
                return jsonify(payload)


api_controller = ApiController()
