import os
from dotenv import load_dotenv
load_dotenv()

main_url = os.getenv("MAIN_URL")
api_key = os.getenv("API_KEY")
