from db import db


class CoinModel(db.Model):
    __tablename__ = "coins"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    symbol = db.Column(db.String(80), nullable=False)
    coin_id = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_by_id(cls, _id: int) -> "CoinModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, _id: int) -> None:
        db.session.delete(self)
        db.session.commit()
