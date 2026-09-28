import json
import requests
from config import main_url , api_key
from pdf_service.generate_pdf import create_pdf

def find_ip(ip) :
    url = main_url + str(ip)
    params = {"access_key" : api_key}
    response = requests.get(url=url , params=params)
    create_pdf(response.json())
    return True

data = find_ip("74.125.24.100")
print(json.dumps(data , indent=4))