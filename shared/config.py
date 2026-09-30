import os
from dotenv import load_dotenv

load_dotenv()

GATEWAY_HOST = os.getenv("GATEWAY_HOST", "127.0.0.1")
GATEWAY_PORT = int(os.getenv("GATEWAY_PORT", "8000"))

DOWNSTREAM_HOST = os.getenv("DOWNSTREAM_HOST", "127.0.0.1")
DOWNSTREAM_PORT = int(os.getenv("DOWNSTREAM_PORT", "5001"))

FLASK_DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

POSTGRES_ADMIN_USER = os.getenv("POSTGRES_ADMIN_USER", "postgres")
POSTGRES_ADMIN_PASSWORD = os.getenv("POSTGRES_ADMIN_PASSWORD")

POSTGRES_APP_USER = os.getenv("POSTGRES_APP_USER", "apex_user")
POSTGRES_APP_PASSWORD = os.getenv("POSTGRES_APP_PASSWORD")

POSTGRES_DB = os.getenv("POSTGRES_DB", "apex_gateway")

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{POSTGRES_APP_USER}:{POSTGRES_APP_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

