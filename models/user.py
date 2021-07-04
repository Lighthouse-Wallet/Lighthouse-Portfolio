from requests import Response
from flask import request, url_for

from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(), nullable=False, unique=True)

    @classmethod
    def find_by_uuid(cls, uuid: str) -> "UserModel":
        return cls.query.filter_by(uuid=uuid).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
