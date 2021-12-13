import traceback
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
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
        user_id = get_jwt_identity()
        portfolio = PortfolioModel.find_by_name(user_id, portfolio_name)
        if not portfolio:
            return {"message": gettext("portfolio_not_found").format(portfolio_name)}, 404
        return {"portfolio": portfolio_schema.dump(portfolio)}, 200

    @classmethod
    @jwt_required()
    def post(cls, portfolio_name: str) -> "PortfolioModel":
        user_id = get_jwt_identity()
        portfolio = portfolio_schema.load({"portfolio_name": portfolio_name, "user_id": user_id})
        if PortfolioModel.find_by_name(user_id, portfolio_name):
            return {"message": gettext("portfolio_exists").format(portfolio_name)}, 400

        try:
            portfolio.save_to_db()
            return {"message": gettext("portfolio_created").format(portfolio_name), "data": portfolio_schema.dump(portfolio)}, 201
        except:
            traceback.print_exc()
            portfolio.delete_from_db()
            return {"message": gettext("portfolio_error_creating")}, 500


class UserPortfolioList(Resource):
    @classmethod
    @jwt_required()
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": gettext("user_not_found")}, 400

        return {"user_portfolios": portfolio_list_schema.dump(PortfolioModel.find_by_id(user_id))}, 200

