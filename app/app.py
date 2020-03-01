from flask import Flask
from .config import Configuration

app = Flask(__name__, template_folder="views")
config = Configuration.Configuration()
app.secret_key = config.secret_key

if __name__ == "__main__":
    #    context = ('ssl.cert', 'ssl.key') # certificate and key file. Cannot be self signed certs
    # app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)  # will listen on port 5000
    app.run(host=config.host, threaded=True, debug=config.debug, port=config.port)

# https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0
