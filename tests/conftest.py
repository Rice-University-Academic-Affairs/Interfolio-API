import pytest
from src.interfolio_api.interfolio_far import InterfolioFAR
from src.interfolio_api.interfolio_core import InterfolioCore


@pytest.fixture
def far():
    return InterfolioFAR(
        database_id="id", public_key="public_key", private_key="private_key"
    )


@pytest.fixture
def core():
    class SimpleConfig:
        pass

    config = SimpleConfig()
    config.public_key = "public_key"
    config.private_key = "private_key"
    config.host = "host"
    config.database_id = "database_id"
    return InterfolioCore(config)
