from ma import ma
from models.portfolio import PortfolioModel


class PortfolioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PortfolioModel
        dump_only = ("id",)
        load_instance = True
        include_fk = True

