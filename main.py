import json
import time
import requests

today = int(time.time())
data = [
    {
        "name": "Nvidia",
        "date": today,
        "rating":0,
        "sale":0
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
url = "https://stin-2025.onrender.com"
testurl = "http://127.0.0.1:5000/"
payload = json.dumps(data)

response = requests.post(f"{testurl}/salestock", json=payload, headers={'Content-type': 'application/json'})
print(response)