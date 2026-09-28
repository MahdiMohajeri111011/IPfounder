import json
import requests
from config import main_url , api_key

def find_ip(ip) :
    url = main_url + str(ip)
    params = {"access_key" : api_key}
    respone = requests.get(url=url , params=params)
    return respone.json()

data = find_ip("74.125.24.100")
print(json.dumps(data , indent=4))