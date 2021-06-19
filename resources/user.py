from flask_restful import Resource
from flask import request
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
import traceback
from models.user import UserModel
from schemas.user import UserSchema
from libs.strings import gettext

user_schema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_uuid(user.uuid):
            return {"message": gettext("user_uuid_exists")}, 400

        try:
            user.save_to_db()
            return {"message": gettext("user_registered")}, 201
        except:
            traceback.print_exc()
            user.delete_from_db()
            return {"message": gettext("user_error_creating")}, 500


class User:
    """
    Resource to be used for testing purposes only. Do not expose in routes.
    """

    @classmethod
    def get(cls, uuid: str):
        user = UserModel.find_by_uuid(uuid=uuid)
        if not user:
            return {"message": gettext("user_not_found")}, 404

        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, uuid: str):
        user = UserModel.find_by_uuid(uuid=uuid)
        if not user:
            return {"message": gettext("user_not_found")}, 404

        user.delete_from_db()
        return {"message": gettext("user_deleted")}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)

        user = UserModel.find_by_uuid(user_data.uuid)

        if user:
            access_token = create_access_token(user.id, fresh=True)
            return {"access_token": access_token}, 200

        return {"message", gettext("user_invalid_credentials")}, 401


class UserLogout(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        user_id = get_jwt_identity()
        return {"message": gettext("user_logged_out").format(user_id)}, 200