from db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class PortfolioModel(db.Model):
    __tablename__ = "portfolios"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    portfolio_name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("UserModel")
    transactions = db.relationship('TransactionModel', lazy='dynamic')

    @classmethod
    def find_by_id(cls, _id: int) -> "PortfolioModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, user_id: str, portfolio_name: str) -> "PortfolioModel":
        return cls.query.filter_by(user_id=user_id, portfolio_name=portfolio_name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, _id: int) -> None:
        db.session.delete(self)
        db.session.commit()

