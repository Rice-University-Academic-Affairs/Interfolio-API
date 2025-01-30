import datetime
import hmac
import hashlib
import base64
import requests
import json

from urllib.parse import urlunsplit, urlencode


class InterfolioBase:
    def __init__(self, config):
        self.config = config

    def _build_and_send_request(
        self, api_endpoint, api_method, payload=None, form_data=None, files=None, **query_params
    ):
        api_url = self._build_api_url(api_endpoint, **query_params)
        headers = self._build_headers(api_endpoint, api_method, **query_params)
        if api_method == "GET": 
            return self._make_get_request(api_url, headers)
        elif api_method == "POST":
            payload = payload if payload is not None else dict()
            return self._make_post_request(api_url, headers, payload, form_data, files)
        elif api_method == "PUT":
            payload = payload if payload is not None else dict()
            return self._make_put_request(api_url,headers, payload)
        elif api_method == "DELETE":
            return self._make_delete_request(api_url, headers)

        else:
            raise ValueError(
                "Currently, the interfolio_api package only supports GET and POST requests."
            )

    @staticmethod
    def _make_get_request(api_url, headers):
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            return json.loads(response.text)
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    @staticmethod
    def _make_delete_request(api_url, headers):
        try:
            response = requests.delete(api_url, headers=headers)
            response.raise_for_status()
            return
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    @staticmethod
    def _make_put_request(api_url, headers, payload):
        try:
            response = requests.put(api_url, headers=headers, json=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    @staticmethod
    def _make_post_request(api_url, headers, payload, form_data=None, files=None):
        print("posting")
        try:
            if files:
                response = requests.post(api_url, headers=headers, data=form_data, files=files)
            else:
                response = requests.post(api_url, headers=headers, json=payload)
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
