# -*- coding: utf-8 -*-
"""

    mslib.mscolab.server
    ~~~~~~~~~~~~~~~~~~~~

    Server for mscolab module

    This file is part of mss.

    :copyright: Copyright 2019 Shivashis Padhi
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from flask import Flask, request, jsonify, send_from_directory
import logging

from mslib.mscolab.models import User, db
from mslib.mscolab.conf import SQLALCHEMY_DB_URI
from mslib.mscolab.sockets_manager import socketio as sockio

# set the project root directory as the static folder
app = Flask(__name__, static_url_path='')
sockio.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DB_URI
app.config['SECRET_KEY'] = 'secret!'
db.init_app(app)


@app.route("/")
def hello():
    return("Testing mscolab server")


def check_login(emailid, password):
    user = User.query.filter_by(emailid=str(emailid)).first()
    if user:
        if user.verify_password(password):
            return(user)
    return(False)


@app.route('/token', methods=["POST"])
def get_auth_token():
    emailid = request.values['emailid']
    password = request.values['password']
    user = check_login(emailid, password)
    if user:
        token = user.generate_auth_token()
        return(jsonify({'token': token.decode('ascii')}))
    else:
        logging.debug("Unauthorized user: %s".format(emailid))
        return("False")


@app.route('/test_authorized')
def authorized():
    token = request.values['token']
    user = User.verify_auth_token(token)
    if user:
        return("True")
    else:
        return("False")


def register_user(email, password, username):
    user = User(email, username, password)
    user_exists = User.query.filter_by(emailid=str(email)).first()
    if user_exists:
        return('False')
    user_exists = User.query.filter_by(username=str(username)).first()
    if user_exists:
        return('False')
    db.session.add(user)
    db.session.commit()
    return('True')


@app.route("/register", methods=["POST"])
def user_register_handler():
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    return(register_user(email, password, username))


@app.route('/get_socket_testfile')
def socket_testfile():
    return send_from_directory('test', 'one.html')


if __name__ == '__main__':
    sockio.run(app, port=8083)