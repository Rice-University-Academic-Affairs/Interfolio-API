import hmac
import hashlib
import base64
from src.interfolio_api.interfolio_far import InterfolioFAR
from freezegun import freeze_time
from unittest import mock


class TestInterfolioCore:
    def test__build_and_send_request(self, core):
        api_endpoint = "/endpoint"
        api_method = "GET"
        query_params = {"param": "value"}

        expected_url = core._build_api_url(api_endpoint, **query_params)
        expected_headers = core._build_headers(api_endpoint, api_method)

        with mock.patch.object(core, "_make_request") as _make_request_mock:
            core._build_and_send_request(api_endpoint, api_method, **query_params)
            _make_request_mock.assert_called_with(expected_url, expected_headers)

    def test_api_url(self, core):
        api_endpoint = "/endpoint"
        query_params = {"a": 1, "b": 2}
        expected_url = f"https://{core.config.host}/endpoint?a=1&b=2"
        assert core._build_api_url(api_endpoint, **query_params) == expected_url

    @freeze_time("1994-12-02 10:00:00")
    def test__build_headers(self, core):
        api_endpoint = "/endpoint"
        api_method = "GET"
        message = core._build_message(
            api_endpoint, api_method, core._create_timestamp()
        )
        signature = core._build_signature(message)

        assert core._build_headers(api_endpoint, api_method) == {
            "TimeStamp": core._create_timestamp(),
            "Authorization": core._build_authentication_header(signature),
            "INTF-DatabaseID": core.config.database_id,
        }

    @freeze_time("1994-12-02 10:00:00")
    def test__create_timestamp(self):
        assert InterfolioFAR._create_timestamp() == "1994-12-02 10:00:00"

    def test__build_signature(self, core):
        message = "message"
        signature_bytes = hmac.new(
            core.config.private_key.encode(), message.encode(), hashlib.sha1
        ).digest()
        signature = base64.b64encode(signature_bytes).decode()
        assert core._build_signature(message) == signature

    def test__build_authentication_header(self, core):
        signature = "signature"
        assert (
            core._build_authentication_header(signature)
            == f"INTF {core.config.public_key}:{signature}"
        )
