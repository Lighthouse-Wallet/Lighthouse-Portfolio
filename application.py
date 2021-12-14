import os
import datetime
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from marshmallow import ValidationError
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

from db import db
from ma import ma
from resources.user import UserRegister, UserLogin
from resources.portfolio import Portfolio, UserPortfolioList
from resources.transaction import Transaction, CreateTransaction

application = app = Flask(__name__)
CORS(application)

### swagger specific ###
SWAGGER_URL = '/'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Lighthouse Portfolio"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

load_dotenv(".env", verbose=True)
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTINGS")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = os.environ.get("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(days=10)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=10)
api = Api(app)
jwt = JWTManager(app)

migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


api.add_resource(UserRegister, "/api/v1/register")
api.add_resource(UserLogin, "/api/v1/login")
api.add_resource(Portfolio, "/api/v1/portfolio/<string:portfolio_name>")
api.add_resource(CreateTransaction, "/api/v1/transaction-create")
api.add_resource(Transaction, "/api/v1/transaction/<uuid:transaction_id>")

# api.add_resource(UserPortfolioList, "/api/v1/portfolio/<int:user_id>")
# api.add_resource(User, "/api/v1/user/<string:uuid>")

db.init_app(app)
if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=8000, debug=True)
