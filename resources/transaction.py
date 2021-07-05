import traceback
from datetime import datetime
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.transaction import TransactionSchema
from models.transaction import TransactionModel
from models.portfolio import PortfolioModel
from schemas.portfolio import PortfolioSchema
from libs.strings import gettext


transaction_schema = TransactionSchema()
portfolio_schema = PortfolioSchema()
transaction_list_schema = TransactionSchema(many=True)


class Transaction(Resource):
    @classmethod
    @jwt_required()
    def get(cls, transaction_id: int) -> "TransactionModel":
        user_id = get_jwt_identity()
        transaction = TransactionModel.find_by_id(user_id, transaction_id)
        if not transaction:
            return {"message": gettext("transaction_not_found").format(transaction_id)}, 404
        return {"portfolio": transaction_schema.dump(transaction)}, 200

    @classmethod
    @jwt_required()
    def put(cls, transaction_id: int):
        return

    @classmethod
    @jwt_required()
    def delete(cls, transaction_id: int):
        return


class CreateTransaction(Resource):
    @classmethod
    @jwt_required()
    def post(cls) -> "TransactionModel":
        user_id = get_jwt_identity()
        transaction_json = request.get_json()

        # Portfolio belongs to user
        portfolio = PortfolioModel.find_by_id(transaction_json['portfolio_id'])
        port_dict = portfolio_schema.dump(portfolio)

        if port_dict['user_id'] != user_id:
            return {"message": gettext("transaction_unauthorized")}, 403

        new_date = str(datetime.fromtimestamp(transaction_json['purchase_date'] / 1000.0))
        transaction_json['purchase_date'] = new_date

        transaction = transaction_schema.load(transaction_json)

        try:
            transaction.save_to_db()
            saved_transaction = transaction_schema.dump(transaction)
            return {"message": gettext("transaction_created"), "data": saved_transaction}, 201
        except:
            traceback.print_exc()
            transaction.delete_from_db()
            return {"message": gettext("transaction_error_creating")}, 500

