from flask import request
from flask import render_template
from flask import Blueprint, request, json
from flask import Flask, request, render_template, send_from_directory, make_response, jsonify
from flask import flash, redirect, session, abort
import os

from app.helper import helper
from ..config import Configuration

config = Configuration.Configuration()


class StaticController:

    def __init__(self):
        pass

    @staticmethod
    def static_proxy(path):
        return send_from_directory(config.root, path, cache_timeout=30 * 60)


static_controller = StaticController()
