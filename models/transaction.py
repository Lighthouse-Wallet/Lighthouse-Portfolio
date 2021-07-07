from db import db


class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.DateTime, nullable=False)
    coin_amount = db.Column(db.Float, nullable=False)
    spot_price = db.Column(db.Float, nullable=False)
    exchange = db.Column(db.String(40), nullable=False)
    fiat = db.Column(db.String(40), nullable=False)
    coin_id = db.Column(db.Integer, nullable=False)
    portfolio_id = db.Column(db.Integer, db.ForeignKey("portfolios.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    portfolio = db.relationship("PortfolioModel")
    user = db.relationship("UserModel")

    @classmethod
    def find_by_filter(cls, _id: int, user_id: int) -> "TransactionModel":
        return cls.query.filter_by(id=_id, user_id=user_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def update_to_db(self, data):
        for k, v in data.items():
            setattr(self, k, v)
        db.session.commit()

    def delete_from_db(self, _id: int) -> None:
        db.session.delete(self)
        db.session.commit()

