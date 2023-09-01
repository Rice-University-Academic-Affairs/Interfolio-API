import pytest
import hmac
import hashlib
import base64
import src.interfolio_far
from src.interfolio_far import InterfolioFAR
from src.constants import dev_config
from freezegun import freeze_time
from unittest import mock


@pytest.fixture
def far():
    return create_fake_far_object()


def create_fake_far_object():
    return InterfolioFAR(
        database_id="id", public_key="public_key", private_key="private_key"
    )


def request_made_with_correct_arguments(
    far_method, api_endpoint, api_method, *method_params, **query_params
):
    far = create_fake_far_object()
    with mock.patch.object(
        src.interfolio_far.InterfolioFAR, "_make_request"
    ) as _make_request_mock:
        headers = far._build_headers(api_endpoint, api_method)
        api_url = far._build_api_url(api_endpoint, **query_params)
        far_method(*method_params, **query_params)
        _make_request_mock.assert_called_with(api_url, headers)


class TestInterfolioFAR:
    def test_initialization(self):
        public_key = "fake_pubic_key"
        private_key = "fake_private_key"
        database_id = "fake_database_id"
        far_api = InterfolioFAR(
            database_id=database_id, public_key=public_key, private_key=private_key
        )
        assert far_api.config.public_key == public_key
        assert far_api.config.private_key == private_key
        assert far_api.config.database_id == database_id

    # def test_api_connection(self):
    #     dev_far = InterfolioFAR(
    #         dev_config.database_id, dev_config.public_key, dev_config.private_key
    #     )
    #     assert dev_far.get_units(data="count").status_code == 200

    def test_get_users(self, far):
        api_endpoint = "/users"
        api_method = "GET"
        query_params = {"employmentstatus": "Full Time"}
        request_made_with_correct_arguments(
            far.get_users, api_endpoint, api_method, **query_params
        )

    def test_get_terms(self, far):
        api_endpoint = "/terms"
        api_method = "GET"
        query_params = {"yearlist": "2017,2018"}
        request_made_with_correct_arguments(
            far.get_terms, api_endpoint, api_method, **query_params
        )

    def test_get_units(self, far):
        api_endpoint = "/units"
        api_method = "GET"
        query_params = {"data": "count"}
        request_made_with_correct_arguments(
            far.get_units, api_endpoint, api_method, **query_params
        )

    def test_get_unit(self, far):
        unit_id = 2
        api_endpoint = f"/units/{unit_id}"
        api_method = "GET"
        query_params = {"data": "count"}
        request_made_with_correct_arguments(
            far.get_unit, api_endpoint, api_method, unit_id, **query_params
        )

    def test__build_and_send_request(self, far):
        api_endpoint = "/endpoint"
        api_method = "GET"
        query_params = {"param": "value"}

        expected_url = far._build_api_url(api_endpoint, **query_params)
        expected_headers = far._build_headers(api_endpoint, api_method)

        with mock.patch.object(
            src.interfolio_far.InterfolioFAR, "_make_request"
        ) as _make_request_mock:
            far._build_and_send_request(api_endpoint, api_method, **query_params)
            _make_request_mock.assert_called_with(expected_url, expected_headers)

    def test_api_url(self, far):
        api_endpoint = "/endpoint"
        query_params = {"a": 1, "b": 2}
        expected_url = "https://faculty180.interfolio.com/api.php/endpoint?a=1&b=2"
        assert far._build_api_url(api_endpoint, **query_params) == expected_url

    @freeze_time("1994-12-02 10:00:00")
    def test__build_headers(self, far):
        api_endpoint = "/endpoint"
        api_method = "GET"
        message = far._build_message(api_endpoint, api_method, far._create_timestamp())
        signature = far._build_signature(message)

        assert far._build_headers(api_endpoint, api_method) == {
            "TimeStamp": far._create_timestamp(),
            "Authorization": far._build_authentication_header(signature),
            "INTF-DatabaseID": far.config.database_id,
        }

    @freeze_time("1994-12-02 10:00:00")
    def test__create_timestamp(self):
        assert InterfolioFAR._create_timestamp() == "1994-12-02 10:00:00"

    def test__build_signature(self, far):
        message = "message"
        signature_bytes = hmac.new(
            far.config.private_key.encode(), message.encode(), hashlib.sha1
        ).digest()
        signature = base64.b64encode(signature_bytes).decode()
        assert far._build_signature(message) == signature

    def test__build_authentication_header(self, far):
        signature = "signature"
        assert (
            far._build_authentication_header(signature)
            == f"INTF {far.config.public_key}:{signature}"
        )
