from db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class PortfolioModel(db.Model):
    __tablename__ = "portfolios"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    portfolio_name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    user = db.relationship("UserModel")
    transactions = db.relationship('TransactionModel', lazy='dynamic')

    @classmethod
    def find_by_id(cls, _id: uuid) -> "PortfolioModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, user_id: uuid, portfolio_name: str) -> "PortfolioModel":
        return cls.query.filter_by(user_id=user_id, portfolio_name=portfolio_name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, _id: uuid) -> None:
        db.session.delete(self)
        db.session.commit()

