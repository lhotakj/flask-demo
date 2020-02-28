#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from app.controller.StaticController import static_controller

static = Blueprint("static", __name__)


@static.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return static_controller.static_proxy(path)
