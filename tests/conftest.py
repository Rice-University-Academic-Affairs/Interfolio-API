import pytest
from src.interfolio_api.interfolio_far import InterfolioFAR
from src.interfolio_api.interfolio_fs import InterfolioFS
from src.interfolio_api.interfolio_base import InterfolioBase
from unittest import mock


@pytest.fixture
def far():
    return InterfolioFAR(
        database_id="id", public_key="public_key", private_key="private_key"
    )


@pytest.fixture
def fs():
    return InterfolioFS(
        tenant_id="id", public_key="public_key", private_key="private_key"
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
    return InterfolioBase(config)


def assert_request_made_with_correct_arguments(api_object, method_name, api_endpoint, api_method, *args, **query_params):
    with mock.patch.object(api_object, "_build_and_send_request") as _build_and_send_request_mock:
        method = getattr(api_object, method_name)
        method(*args, **query_params)
        _build_and_send_request_mock.assert_called_with(api_endpoint, api_method, **query_params)
