from sqlalchemy.dialects.postgresql import UUID
import uuid

from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    device_id = db.Column(db.String(), nullable=False, unique=True)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @classmethod
    def find_by_device_id(cls, value: str) -> "UserModel":
        return cls.query.filter_by(device_id=value).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
