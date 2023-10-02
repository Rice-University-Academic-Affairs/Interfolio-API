import pytest
from src.interfolio_api.interfolio_far import InterfolioFAR
from src.interfolio_api.interfolio_fs import InterfolioFS
from src.interfolio_api.interfolio_core import InterfolioCore
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
    return InterfolioCore(config)


def assert_request_made_with_correct_arguments(
    api_object,
    api_object_method_name,
    api_endpoint,
    api_method,
    *method_params,
    **query_params,
):
    with mock.patch.object(api_object, "_make_request") as _make_request_mock:
        expected_headers = api_object._build_headers(
            api_endpoint, api_method, **query_params
        )
        expected_api_url = api_object._build_api_url(api_endpoint, **query_params)
        method_under_test = getattr(api_object, api_object_method_name)
        method_under_test(*method_params, **query_params)
        _make_request_mock.assert_called_with(expected_api_url, expected_headers)
