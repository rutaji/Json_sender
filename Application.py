import json
import os

import requests
from flask import Flask, request, jsonify, render_template, redirect

from Examples import example1
from Form import JsonForm
testurl = "http://127.0.0.1:5000/"

app = Flask(__name__)

input = example1
app.config["SECRET_KEY"] = os.environ.get("SECRET","dev")
url = "https://stin-2025.onrender.com/"
output =""
output_code = 0

@app.route('/')
def home():
    return redirect("/test-liststock", code=302)

@app.route('/test-liststock',methods=['GET','POST'])
def liststock():
    global output_code,input
    form = JsonForm(input = input)
    if form.validate_on_submit():
        input = form.input.data
        payload = json.dumps(input)
        response = requests.post(f"{testurl}/liststock", json=payload)
        output_code = response.status_code
    return render_template("liststock.html",form = form,output_code = output_code)

@app.route('/test-salestock',methods=['GET','POST'])
def salestock():
    global output_code, input
    form = JsonForm(input=input)
    if form.validate_on_submit():
        input = form.input.data
        data = [
            {"name": "OpenAI", "date": 12345678, "rating": 2, "sale": 0}
        ]

        payload = json.dumps(data)
        print(payload)
        response = requests.post(f"{testurl}/salestock", json=input,headers={'Content-type': 'application/json','Accept': 'application/json'})
        output_code = response.status_code
        out = response.json
        pass
    return render_template("salestock.html",form = form,output_code = output_code)



