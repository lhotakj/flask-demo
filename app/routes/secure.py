#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from app.controller.SecureController import secure_controller

secure = Blueprint("secure", __name__)


@secure.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    return secure_controller.do_admin_login()
