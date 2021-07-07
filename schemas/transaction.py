from ma import ma
from models.transaction import TransactionModel
from models.portfolio import PortfolioModel


class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TransactionModel
        # load_only = ("transaction",)
        dump_only = ("id",)
        load_instance = True
        include_fk = True

