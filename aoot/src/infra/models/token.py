import sqlalchemy as sa

from src.domain.tokens import Token, Ticker

from .base import METADATA, MAPPER_REGISTRY


class TickerSQLAlchemyType(sa.TypeDecorator):
    impl = sa.Text
    cache_ok = True

    def process_bind_param(self, ticker: Ticker, dialect) -> str:
        return ticker.value

    def process_result_value(self, ticker: str, dialect) -> Ticker:
        return Ticker(ticker)


TOKENS_TABLE = sa.Table(
    "tokens",
    METADATA,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("ticker", TickerSQLAlchemyType(), nullable=False),
    sa.Column("is_buyed", sa.Boolean, default=False, nullable=False),
)

MAPPER_REGISTRY.map_imperatively(
    Token, TOKENS_TABLE, properties={"_is_buyed": TOKENS_TABLE.c.is_buyed}
)
