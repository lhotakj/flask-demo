#!/usr/bin/python
# -*- coding: utf-8 -*-
from app.config import Configuration

from flask import Flask, request, render_template, send_from_directory, make_response, jsonify

config = Configuration.Configuration()


def skeleton(template, **kwargs):
    kwargs["version"] = config.version
    kwargs["version_sha"] = config.version_sha
    kwargs["version_url"] = config.version_url
    return render_template(template_name_or_list=template, **kwargs)


def only_get_method(func):
    def function_wrapper(*args):
        if request.method == 'GET':
            return skeleton(template="api-error.html", title="API error")
        return func(*args)

    return function_wrapper
