import requests, random, json
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/dankmemes/.json"
def request_JSON(url):
    json = requests.get(url, headers = {'User-agent': 'your bot 0.1'}).json()
    return json

def load_json(json_data):
    children = json_data.get("data").get("children")
    return children

def parse_json(children):
    for node in children:
        post = node["data"]
        print(post)
        

#print(request_JSON(url))
#print(load_json(request_JSON(url)))
print(parse_json(load_json(request_JSON(url))))