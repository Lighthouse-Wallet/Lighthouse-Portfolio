from ma import ma
from models.portfolio import PortfolioModel
from models.transaction import TransactionModel
from schemas.transaction import TransactionSchema


class PortfolioSchema(ma.SQLAlchemyAutoSchema):
    transactions = ma.Nested(TransactionSchema, many=True)

    class Meta:
        model = PortfolioModel
        dump_only = ("id",)
        load_instance = True
        include_fk = True

