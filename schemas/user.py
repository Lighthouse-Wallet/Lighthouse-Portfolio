from ma import ma
from models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        dump_only = ("id",)
        load_instance = True
        include_fk = True
