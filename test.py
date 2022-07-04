from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "HTML", "views": 100000},
        {"likes": 100, "name": "CSS", "views": 1000000},
        {"likes": 1000, "name": "Javascript", "views": 10000000},
        {"likes": 10000, "name": "Python", "views": 100000000}]

for i in range(len(data)):
    response = requests.put(
        BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/6")
print(response.json())
