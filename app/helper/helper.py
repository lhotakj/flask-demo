#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, request, render_template, send_from_directory, make_response, jsonify


def skeleton(template, **kwargs):
    return render_template(template_name_or_list=template, **kwargs)


def only_get_method(func):
    def function_wrapper(*args):
        if request.method == 'GET':
            return skeleton(template="api-error.html", title="API error")
        func(*args)

    return function_wrapper
