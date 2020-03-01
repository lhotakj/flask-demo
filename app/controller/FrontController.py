from flask import request
from flask import render_template
from flask import Blueprint, request, json
from flask import Flask, request, render_template, send_from_directory, make_response, jsonify
from flask import flash, redirect, session, abort

from app.helper import helper


class FrontController:

    def __init__(self):
        pass

    @staticmethod
    def my_instances():
        return helper.skeleton(template="my-instances.html", title="my instances")

    @staticmethod
    def monitoring():
        return helper.skeleton(template="monitoring.html", title="monitoring")

    @staticmethod
    def how_to():
        return helper.skeleton(template="how-to.html", title="how to")

    @staticmethod
    def root():
        return helper.skeleton(template="overview.html", title="Overview")

    @staticmethod
    def logout():
        session['logged_in'] = False
        session['username'] = None
        return helper.skeleton(template="logout.html", title="logout")

    @staticmethod
    def do_admin_login():
        if request.form and 'password' in request.form and 'username' in request.form:
            if request.form['password'] == 'password' and request.form['username'] == 'admin':
                session['logged_in'] = True
                session['username'] = request.form['username']
                session['full_name'] = "Antonius Blbus"
            else:
                flash(message='Invalid credentials! Make sure you use your OAAD account in format AB123',
                      category='danger')
        return helper.skeleton(template="login.html", title="login")


front_controller = FrontController()
