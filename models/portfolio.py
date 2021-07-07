from db import db


class PortfolioModel(db.Model):
    __tablename__ = "portfolios"

    id = db.Column(db.Integer, primary_key=True)
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

