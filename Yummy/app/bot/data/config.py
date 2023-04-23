# there are all parameters from .env file
import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
admins = os.getenv('ADMIN_ID')
ADMIN_ID = admins.split()