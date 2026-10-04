import re
import json
import requests
from config import main_url , api_key
from email_service.send_email import send_email
from pdf_service.generate_pdf import create_pdf

EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def email_checker(email) :

    while not re.match(EMAIL_PATTERN , email) :
        email = input("Enter a valid email or exit with [q]")

        if email == "q" :
            return False

    return True



def find_ip(ip) :

    url = main_url + str(ip)
    params = {"access_key" : api_key}
    response = requests.get(url=url , params=params)
    data = response.json()


    q1 = input("Would you like the result to be sent to you as an email? [y/n]")

    if q1 == "y" :
        email = input("Enter your email")
        result = email_checker(email)

        if result is True :
            pdf = create_pdf(response.json())
            send_email(pdf , email)

    else :
        return json.dumps(data , indent=4)


ip = input("Enter IP : ")
print(find_ip(ip))

