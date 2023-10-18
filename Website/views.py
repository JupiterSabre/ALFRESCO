from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import requests
from .models import User, Route_Instance
from . import db

from flask_socketio import join_room, leave_room, send, SocketIO

# import random
# from string import ascii_uppercase

# socketio= SocketIO(app)
# rooms = {}

# def generate_unique_code(length):
#     while True:
#         code = ""
#         for _ in range(length):
#             code += random.choice(ascii_uppercase)
#         if code not in rooms:
#             break
#     return code




views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    print("Hi I am a route")
    return render_template("home.html", user=current_user)


@views.route("/map", methods=["GET", "POST"])
def map_view():
    print("Hi I am the map route")
    return render_template("map.html", user=current_user)