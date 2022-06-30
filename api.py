import requests
import json

URL = "http://127.0.0.1:8000/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data=json_data)
    extract_data = r.json()
    print(extract_data)
# get_data(1)


def post_data():
    data = {
        'name':'Raja Kumar',
        'roll':220,
        'city':'Dhanbad'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    res = r.json()
    print(res)
# post_data()

def update_data():
    data = {
        'id':5,
        'name':'Sohan Purbiya',
        'roll':'220',
        'city':'Bhestan'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    res = r.json()
    print(res)
update_data()


def delete_data():
    data = {'id':5}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    res = r.json()
    print(res)
# delete_data()