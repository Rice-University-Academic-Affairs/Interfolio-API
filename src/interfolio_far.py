import datetime
import hmac
import hashlib
import base64
import requests
from src.interfolio_far_config import InterfolioFARConfig


class InterfolioFAR:
    def __init__(self, database_id=None, public_key=None, private_key=None):
        self.config = InterfolioFARConfig(
            database_id=database_id, public_key=public_key, private_key=private_key
        )

    def get_units(self, data: str, unit_id=None, limit: int = None, offset: int = None):
        """
        :param unit_id: ID of academic unit
        :param data: count, summary, or detailed
        :param limit: limits number returned
        :param offset: offset for paginating values
        https://www.faculty180.com/swagger/ui/index.html#section/Standard-GET-Parameters-Used
        """
        timestamp = self._create_timestamp()
        api_endpoint = "/units"
        api_method = "GET"
        query_params = f"?data={data}"
        message = self._build_message(api_method, timestamp, api_endpoint)
        signature = self._generate_signature(message, self.config.private_key)
        auth_header = self._build_header(signature)
        api_url = self.config.host + api_endpoint + query_params
        headers = {
            "TimeStamp": timestamp,
            "Authorization": auth_header,
            "INTF-DatabaseID": self.config.database_id,
        }
        response = requests.get(api_url, headers=headers)
        response_text = response.text
        print("Response:", response_text)

    def _build_message(self, api_method, timestamp, request_string):
        return f"{api_method}\n\n\n{timestamp}\n{request_string}"

    @staticmethod
    def _generate_signature(message, private_key):
        signature_bytes = hmac.new(
            private_key.encode(), message.encode(), hashlib.sha1
        ).digest()
        return base64.b64encode(signature_bytes).decode()

    @staticmethod
    def _create_timestamp():
        return datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def _build_header(self, signature):
        return f"INTF {self.config.public_key}:{signature}"
