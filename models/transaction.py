from db import db


class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.DateTime, nullable=False)
    coinAmount = db.Column(db.Float, nullable=False)
    spot_price = db.Column(db.Float, nullable=False)
    exchange = db.Column(db.String(40), nullable=False)
    fiat = db.Column(db.String(40), nullable=False)
    coin_id = db.Column(db.Integer, db.ForeignKey("coins.id"), nullable=False)
    portfolio_id = db.Column(db.Integer, db.ForeignKey("portfolios.id"), nullable=False)

    portfolio = db.relationship("PortfolioModel")
    coin = db.relationship("CoinModel", lazy="dynamic")

    @classmethod
    def find_by_id(cls, _id: int) -> "TransactionModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, _id: int) -> None:
        db.session.delete(self)
        db.session.commit()