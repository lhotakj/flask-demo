from flask import request
from flask import render_template
from flask import Blueprint, request, json
from flask import Flask, request, render_template, send_from_directory, make_response, jsonify
from flask import flash, redirect, session, abort
import os

from app.helper import helper

class SecureController:

    def __init__(self):
        pass

    @staticmethod
    def do_admin_login():
        if request.form and 'password' in request.form and 'username' in request.form:
            if request.form['password'] == 'password' and request.form['username'] == 'admin':
                session['logged_in'] = True
                session['username'] = request.form['username']
                session['full_name'] = "Antonius Blbus"
            else:
                flash('wrong password!')
        return helper.skeleton(template="login.html", title="login")


secure_controller = SecureController()
