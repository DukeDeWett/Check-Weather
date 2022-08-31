import requests

def name(request_url):
    reply = requests.get(request_url)
    if reply.status_code == 200:
        data = reply.json()
        name = data['name']
        return name

def description(request_url):
    reply = requests.get(request_url)
    if reply.status_code == 200:
        data = reply.json()
        weather = data['weather'][0]['description']
        return weather