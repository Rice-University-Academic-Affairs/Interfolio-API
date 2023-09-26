import datetime
import hmac
import hashlib
import base64
import requests
import json

from urllib.parse import urlunsplit, urlencode


class InterfolioCore:
    def __init__(self, config):
        self.config = config

    def _build_and_send_request(self, api_endpoint, api_method, **query_params):
        api_url = self._build_api_url(api_endpoint, **query_params)
        headers = self._build_headers(api_endpoint, api_method, **query_params)
        return self._make_request(api_url, headers)

    @staticmethod
    def _make_request(api_url, headers):
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            return json.loads(response.text)
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def _build_api_url(self, api_endpoint, **query_params):
        query = urlencode(query_params)
        url = urlunsplit(("https", self.config.host, api_endpoint, query, ""))
        return url

    def _build_headers(self, api_endpoint, api_method, **query_params):
        timestamp = self._create_timestamp()
        message = self._build_message(
            api_endpoint, api_method, timestamp, **query_params
        )
        signature = self._build_signature(message)
        header = {
            "TimeStamp": self._create_timestamp(),
            "Authorization": self._build_authentication_header(signature),
        }
        if hasattr(self.config, "database_id"):
            header["INTF-DatabaseID"] = self.config.database_id
        return header

    @staticmethod
    def _create_timestamp():
        return datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    @staticmethod
    def _build_message(api_endpoint, api_method, timestamp, **query_params):
        return f"{api_method}\n\n\n{timestamp}\n{api_endpoint}"

    def _build_signature(self, message):
        signature_bytes = hmac.new(
            self.config.private_key.encode(), message.encode(), hashlib.sha1
        ).digest()
        return base64.b64encode(signature_bytes).decode()

    def _build_authentication_header(self, signature):
        return f"INTF {self.config.public_key}:{signature}"
