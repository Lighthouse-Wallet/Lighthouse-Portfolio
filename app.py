from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from marshmallow import ValidationError
from dotenv import load_dotenv

from db import db
from ma import ma
from resources.user import UserRegister, User, UserLogin
from resources.portfolio import Portfolio, UserPortfolioList

app = Flask(__name__)
load_dotenv(".env", verbose=True)
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)
jwt = JWTManager(app)

migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<str:uuid>")  # for testing purposes
api.add_resource(UserLogin, "/register")
api.add_resource(UserPortfolioList, "/portfolio/<int:user_id>")
api.add_resource(Portfolio, "/user/<int:portfolio_id>")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)