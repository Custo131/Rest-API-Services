import os
from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.environ.get("DATABASE_URL", "")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set.")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set.")
