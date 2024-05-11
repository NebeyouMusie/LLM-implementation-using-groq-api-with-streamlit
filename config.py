import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
def load_config():
    load_dotenv()

def get_groq_api_key():
    return os.getenv('GROQ_API_KEY')
