#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from app.controller.FrontController import front_controller

front = Blueprint("front", __name__)


@front.route('/')
def root():
    return front_controller.root()


@front.route('/my-instances')
def my_instances():
    return front_controller.my_instances()


@front.route('/monitoring')
def monitoring():
    return front_controller.monitoring()


@front.route('/how-to')
def how_to():
    return front_controller.how_to()


@front.route('/logout', methods=['GET'])
def logout():
    return front_controller.logout()
