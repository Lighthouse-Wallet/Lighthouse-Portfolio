from ma import ma
from models.transaction import TransactionModel
from models.portfolio import PortfolioModel


class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TransactionModel
        load_only = ("portfolio",)
        dump_only = ("id",)
        include_fk = True

