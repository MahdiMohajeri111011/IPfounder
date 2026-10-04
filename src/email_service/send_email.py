import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib

load_dotenv()


def send_email(pdf , input_email = None) :
    massage = EmailMessage()
    massage["Subject"] = "IP geolocation result"
    massage["From"] = "mahdimohajeri91@gmail.com"
    massage["To"] = input_email
    massage.set_content("Result : ")

    with open("result.pdf" , "rb") as file :
        massage.add_attachment(file.read() , filename = "result.pdf" , maintype = "application" , subtype = "application/pdf")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("MY_GMAIL"), "GMAIL_PASSOWORD")
        smtp.send_message(massage)

