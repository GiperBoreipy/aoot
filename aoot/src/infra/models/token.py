import sqlalchemy as sa

from infra.models.base import METADATA, MAPPER_REGISTRY

from domain.tokens import Token


TOKENS_TABLE = sa.Table(
    "tokens",
    METADATA,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("ticker", sa.Text, nullable=False),
    sa.Column("is_buyed", sa.Boolean, default=False, nullable=False),
)

MAPPER_REGISTRY.map_imperatively(
    Token, TOKENS_TABLE, properties={"_is_buyed": TOKENS_TABLE.c.is_buyed}
)
