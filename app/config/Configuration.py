import os


class Configuration:

    def __init__(self):
        pass

    host = "0.0.0.0"
    root = os.path.dirname(os.path.realpath(__file__))
    secret_key = os.urandom(12)
    verification_token = os.environ['VERIFICATION_TOKEN']
    slack_token = os.environ["SLACK_API_TOKEN"]

    version = "1.0"
    version_sha = "d45aff"  # git log --pretty=format:'%h' -n 1
