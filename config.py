import os

DEBUG = False
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]