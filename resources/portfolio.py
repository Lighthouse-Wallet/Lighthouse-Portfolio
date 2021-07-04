import traceback
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from typing import List
from schemas.portfolio import PortfolioSchema
from models.portfolio import PortfolioModel
from models.user import UserModel
from libs.strings import gettext


portfolio_schema = PortfolioSchema()
portfolio_list_schema = PortfolioSchema(many=True)


class Portfolio(Resource):
    @classmethod
    @jwt_required()
    def get(cls, portfolio_name: str) -> "PortfolioModel":
        # portfolio = PortfolioModel.find_by_id(portfolio_id)
        user_id = get_jwt_identity()
        portfolio = PortfolioModel.find_by_name(user_id, portfolio_name)
        return {"portfolio": portfolio_schema.dump(portfolio)}, 200

    @classmethod
    @jwt_required()
    def post(cls, portfolio_name: str) -> "PortfolioModel":
        user_id = get_jwt_identity()
        if not PortfolioModel.find_by_name(user_id, portfolio_name):
            return {"message": "Not"}

        return {"message": "Success"}, 201



class UserPortfolioList(Resource):
    @classmethod
    @jwt_required()
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": gettext("user_not_found")}, 400

        return {"user_portfolios": portfolio_list_schema.dump(PortfolioModel.find_by_id(user_id))}, 200

