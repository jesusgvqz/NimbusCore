from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_wtf import CSRFProtect
from flasgger import Swagger
from .config import Config
from app.models.user import db, User


csrf = CSRFProtect()
db = SQLAlchemy()
jwt = JWTManager()
swagger = Swagger()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    csrf.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)

    from .routes.auth import auth_bp
    from .routes.login import login_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(login_bp) 

    return app
    