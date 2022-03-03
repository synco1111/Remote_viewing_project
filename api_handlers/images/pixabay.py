from dotenv import load_dotenv
import os

load_dotenv('authentication_utils/.env')
API_KEY = os.getenv("PIXABAY_API_KEY")
