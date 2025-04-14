import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database settings
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")

# define sslmode
SSLMODE = "require" if os.environ.get("DB_SSL", "false").lower() == "true" else "disable"

# API settings
API_DOMAIN = os.environ.get("API_DOMAIN")
API_KEY_HEADER = os.environ.get("API_KEY_HEADER")
API_KEY = os.environ.get("API_KEY")

# Application settings
TABLE_NAME = os.environ.get("TABLE_NAME")
LOG_LEVEL = os.environ.get("LOG_LEVEL")