from db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    purchase_date = db.Column(db.DateTime, nullable=False)
    coin_amount = db.Column(db.Float, nullable=False)
    spot_price = db.Column(db.Float, nullable=False)
    exchange = db.Column(db.String(40), nullable=False)
    fiat = db.Column(db.String(40), nullable=False)
    coin_id = db.Column(db.Integer, nullable=False)
    is_buy = db.Column(db.Boolean, nullable=False)
    price_type = db.Column(db.Integer, nullable=False)
    portfolio_id = db.Column(UUID(as_uuid=True), db.ForeignKey("portfolios.id"), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    portfolio = db.relationship("PortfolioModel")
    user = db.relationship("UserModel")

    @classmethod
    def find_by_filter(cls, _id: uuid, user_id: uuid) -> "TransactionModel":
        return cls.query.filter_by(id=_id, user_id=user_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def update_to_db(self, data):
        for k, v in data.items():
            setattr(self, k, v)
        db.session.commit()

    def delete_from_db(self, _id: uuid) -> None:
        db.session.delete(self)
        db.session.commit()

