import traceback
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
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
    def get(cls, portfolio_id: int) -> "PortfolioModel":
        portfolio = PortfolioModel.find_by_id(portfolio_id)


class UserPortfolioList(Resource):
    @classmethod
    @jwt_required()
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": gettext("user_notFound")}, 400

        return {"user_portfolios": portfolio_list_schema.dump(PortfolioModel.find_by_id(user_id))}, 200

