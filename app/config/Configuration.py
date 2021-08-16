import logging.handlers
import logging.handlers
import os
import subprocess
from logging.handlers import RotatingFileHandler


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(cls, bases, dict)
        cls._instanceDict = {}

    def __call__(cls, *args, **kwargs):
        arg_dictionary = {'args': args}
        arg_dictionary.update(kwargs)
        arg_set = frozenset(arg_dictionary)
        if arg_set not in cls._instanceDict:
            cls._instanceDict[arg_set] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instanceDict[arg_set]


class Configuration(object):
    __metaclass__ = Singleton

    _host = '0.0.0.0'
    _port = 5000
    _version = "1.1"
    _version_sha = ""  # read on application start
    _version_url = ""  # read on application start

    _debug = True
    _root = os.path.dirname(os.path.realpath(__file__))
    _secret_key = os.urandom(12)

    # read from environment variables!
    _verification_token = os.environ['VERIFICATION_TOKEN']
    _slack_token = os.environ["SLACK_API_TOKEN"]

    _admin_users = ['za577', 'rint', 'ke998', 'admin']

    def __init__(self):

        if self._version_sha == "":
            p = subprocess.Popen("git log --pretty=format:'%h' -n 1", stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p.wait()
            if err == 0:
                self._version_sha = output.decode()  # git log --pretty=format:'%h' -n 1
            else:
                self._version_sha = "?"
        else:
            self._version_sha = "?"

        if self._version_url == "":
            u = subprocess.Popen("git config --get remote.origin.url", stdout=subprocess.PIPE, shell=True)
            (output_u, err) = u.communicate()
            u.wait()
            if err == 0:
                self._version_url = output_u.decode().strip()  # git log --pretty=format:'%h' -n 1
                # git@github.com:lhotakj/flask-demo.git >> https://github.com/lhotakj/flask-demo.git
                self._version_url = self._version_url.replace(":", "/")
                self._version_url = self._version_url.replace("git@", "https://")
            else:
                self._version_url = "?"
        else:
            self._version_url = "?"

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def version(self):
        return self._version

    @property
    def version_sha(self):
        return self._version_sha

    @property
    def version_url(self):
        return self._version_url

    @property
    def debug(self):
        return self._debug

    @property
    def root(self):
        return self._root

    @property
    def secret_key(self):
        return self._secret_key

    @property
    def verification_token(self):
        return self._verification_token

    @property
    def slack_token(self):
        return self._slack_token

    @property
    def admin_users(self):
        return self._admin_users

    @staticmethod
    def logger():
        file = os.path.join(os.environ.get("LOG_FOLDER", "/tmp/kratos-web"), "default.log")
        level = os.environ.get("LOG_LEVEL", "INFO")
        logger = logging.getLogger(__name__)
        handler = RotatingFileHandler(file, maxBytes=2000, backupCount=10)
        logger.setLevel(logging.DEBUG)
        level_o = logging.DEBUG

        if level == "DEBUG": level_o = logging.DEBUG
        if level == "INFO": level_o = logging.INFO
        if level == "ERROR": level_o = logging.ERROR
        if level == "WARNING": level_o = logging.WARNING

        logging.basicConfig(
            filename=file,
            level=level_o,
            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )

        logger.handlers.clear()
        #logger.addHandler(handler)

        return logger
