from typing import Final

from sqlalchemy import MetaData
from sqlalchemy.orm import registry


METADATA: Final = MetaData()
MAPPER_REGISTRY: Final = registry(metadata=METADATA)
