import json
import time

today = int(time.time())

example = list()
example.append([
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
 ])

example.append([
    {
        "name": "Nvidia",
        "date": today,
        "rating":0,
        "sale":0
    }
 ])
example.append([

 ])
example.append([
    {
        "name": "errororor",
        "date": today,
        "rating":-8,
    }
 ])

