import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecretkey")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "defaultjwtkey")

    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600))
    JWT_TOKEN_LOCATION = os.getenv("JWT_TOKEN_LOCATION", "headers").split(',')

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://nimbuscore:n1mbus.C0r3@db:5432/nimbuscoredb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
