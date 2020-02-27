from flask import Flask, request, render_template, send_from_directory, make_response, jsonify

import os
import json

document_root = os.path.dirname(os.path.realpath(__file__))

# https://api.slack.com/apps/ATPCVD9JN/general?
# https://dashboard.heroku.com/apps/jarda-demo/settings
verification_token = os.environ['VERIFICATION_TOKEN']

filename = '/tmp/webhookPayloads.txt'  # file that webhook payloads will be written

if os.path.exists(filename):
    append_write = 'a'  # append if already exists
else:
    append_write = 'w'  # make a new file if not

app = Flask(__name__)


def skeleton(**kwargs):
    return render_template('masterpage.html', **kwargs)


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(document_root, path)


@app.route('/api/slack/<string:command>', methods=['POST', 'GET'])
def slack_command(command):
    if request.method == 'GET':
        return skeleton(title="Error",
                        content="Sorry dude but this is an API endpoint and required to be called with POST from SLACK")
    if request.form['token'] == verification_token:
        if command == "my-instances":
            payload = {
                'text': 'Hey dude, this is your list of instances.\n This is the request sent from Slack: ```' + str(
                    request.form) + "```"}
            return jsonify(payload)


@app.route('/api/<string:type>', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return '<h1>Hello from Webhook Listener!a</h1>'
    if request.method == 'POST':
        f = open(filename, append_write)
        req_data = request.get_json()
        str_obj = json.dumps(req_data)
        f.write(str_obj + '\n')
        f.close()
        return '{"success":"true"}'


@app.route('/my-instances')
def myinstances():
    return skeleton(title="My instances", content="list my instances TBD")


@app.route('/monitoring')
def monitoring():
    return skeleton(title="Monitoring", content="monitoring")


@app.route('/how-to')
def how():
    return skeleton(title="How to", content="How to")


@app.route('/')
def root():
    return skeleton(title='home', content="hello")


if __name__ == "__main__":
    #    context = ('ssl.cert', 'ssl.key') # certificate and key file. Cannot be self signed certs
    # app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)  # will listen on port 5000
    app.run(host='0.0.0.0', threaded=True, debug=True)  # will listen on port 5000

# https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0
