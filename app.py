from flask import Flask, render_template, request, redirect, session, url_for, send_file
import requests
import json
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import json
import base64

app = Flask(__name__)

app.config["admin_email"] = "benjamin.glick@ge.com"
app.secret_key = b'\x9b4\xf8%\x1b\x90\x0e[?\xbd\x14\x7fS\x1c\xe7Y\xd8\x1c\xf9\xda\xb0K=\xba'
# I will obviously change this secret key before we go live

nodes_list = ["mayo", "bacon", "lettuce", "tomato", "sprouts"]
services_list = ["dns", "ping", "ssh", "sge"]


@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/index.php')
@app.route('/home')
@app.route('/home.html')
@app.route('/login')
@app.route('/status')
def hello_world():
    """Home Page"""
    return render_template("status.html")
