import traceback
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from typing import List
from schemas.transaction import TransactionSchema
from models.transaction import TransactionModel
from models.user import UserModel
from libs.strings import gettext


transaction_schema = TransactionSchema()
transaction_list_schema = TransactionSchema(many=True)


class Transaction(Resource):
    @classmethod
    @jwt_required()
    def get(cls, transaction_id: int) -> "TransactionModel":
        user_id = get_jwt_identity()
        transaction = TransactionModel.find_by_id(user_id, transaction_id)
        if not transaction:
            return {"message": gettext("transaction_not_found")}, 404
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
        transaction = transaction_schema.load({**transaction_json, user_id: user_id})

        try:
            transaction.save_to_db()
            return {"message": gettext("transaction_created")}, 201
        except:
            traceback.print_exc()
            transaction.delete_from_db()
            return {"message": gettext("transaction_error_creating")}, 500

