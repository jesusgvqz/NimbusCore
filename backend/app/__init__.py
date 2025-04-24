from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load config from config.py
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    Swagger(app)  # <-- enables Swagger UI at /apidocs by default

    # Register blueprints
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app
