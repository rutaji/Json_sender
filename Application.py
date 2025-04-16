import json
import os
import time

import requests
from flask import Flask, request, jsonify, render_template, redirect

from Examples import example
from Form import JsonForm


app = Flask(__name__)
testurl = "http://127.0.0.1:5000/"
input = example[0]
app.config["SECRET_KEY"] = os.environ.get("SECRET","dev")
url = "https://stin-2025.onrender.com/"
output =""
output_code = 0
today = int(time.time())


@app.route('/')
def home():
    return redirect("/test-liststock", code=302)

@app.route('/test-liststock',methods=['GET','POST'])
def liststock():
    global output_code, input, output
    form = JsonForm(input = input)
    if form.validate_on_submit():
        input = form.input.data
        send_data("/liststock")
        pass
    return render_template("liststock.html",form = form,output_code = output_code,output = output)

@app.route('/test-salestock',methods=['GET','POST'])
def salestock():
    global output_code, input, output
    form = JsonForm(input=input)
    if form.validate_on_submit():
        input = form.input.data
        send_data("/salestock")
    return render_template("salestock.html",form = form,output_code = output_code,output = output)


def send_data(endpoint):
    global output_code, input, output
    cuteed =input.replace("\'","\"")
    data = [
        {
            "name": "Nvidia",
            "date": today,
            "rating": 0,
            "sale": 0
        },
        {
            "name": "Microsoft",
            "date": today,
            "rating": 0,
            "sale": 1
        },
        {
            "name": "Amazon",
            "date": today,
            "rating": 0,
            "sale": 1
        }
    ]
    payload = json.dumps(data)
    response = requests.post(f"{url}{endpoint}", json=cuteed,
                             headers={'Content-type': 'application/json', 'Accept': 'application/json'})
    output_code = response.status_code
    output = response.content
    pass


@app.route('/example3')
def ex3():
    global  input
    input = example[3]
    return redirect("/test-liststock", code=302)
@app.route('/example2')
def ex2():
    global input
    input = example[2]
    return redirect("/test-liststock", code=302)
@app.route('/example1')
def ex1():
    global input
    input = example[1]
    return redirect("/test-liststock", code=302)
@app.route('/example0')
def ex0():
    global input
    input = example[0]
    return redirect("/test-liststock", code=302)




