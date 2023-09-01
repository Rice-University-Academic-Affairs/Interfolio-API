import datetime
import hmac
import hashlib
import base64
import requests

from urllib.parse import urlunsplit, urlencode

from src.interfolio_far_config import InterfolioFARConfig


class InterfolioFAR:
    def __init__(self, database_id=None, public_key=None, private_key=None):
        self.config = InterfolioFARConfig(
            database_id=database_id, public_key=public_key, private_key=private_key
        )

    def get_units(self, **query_params):
        """
        :param data: count, summary, or detailed
        :param unit_id: ID of academic unit
        :param limit: limits number returned
        :param offset: offset for paginating values
        https://www.faculty180.com/swagger/ui/index.html#section/Standard-GET-Parameters-Used
        """
        api_endpoint = "/units"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_unit(self, unit_id, **query_params):
        api_endpoint = f"/units/{unit_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_terms(self, **query_params):
        api_endpoint = "/terms"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_users(self, **query_params):
        api_endpoint = "/users"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_user(self, user_id, **query_params):
        api_endpoint = f"/users/{user_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_permissions(self, **query_params):
        api_endpoint = "/users/permissions"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_permission(self, user_id, **query_params):
        api_endpoint = f"/users/{user_id}/permissions"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_faculty_classification_data(self, **query_params):
        api_endpoint = "/facultyclassificationdata"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_faculty_classifications(self, **query_params):
        api_endpoint = "/facultyclassifications"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_faculty_classification(self, faculty_classification_id, **query_params):
        api_endpoint = f"/facultyclassifications/{faculty_classification_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_sections(self, **query_params):
        api_endpoint = "/sections"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_section(self, section_id, **query_params):
        api_endpoint = f"/sections/{section_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activities_ids_in_sections(self, **query_params):
        api_endpoint = "/activities"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activities_ids_for_section(self, section_id, **query_params):
        api_endpoint = f"/activities/{section_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activities_details_for_section(self, section_id, **query_params):
        api_endpoint = f"/activities_details/{section_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activity_details(self, section_id, activity_id, **query_params):
        api_endpoint = f"/activities/{section_id}/{activity_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activity_attachments(self, section_id, activity_id, **query_params):
        api_endpoint = f"/activities/{section_id}/{activity_id}/attachments"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def _build_and_send_request(self, api_endpoint, api_method, **query_params):
        api_url = self._build_api_url(api_endpoint, **query_params)
        headers = self._build_headers(api_endpoint, api_method)
        return self._make_request(api_url, headers)

    @staticmethod
    def _make_request(api_url, headers):
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def _build_api_url(self, api_endpoint, **query_params):
        query = urlencode(query_params)
        url = urlunsplit(("https", self.config.host, api_endpoint, query, ""))
        return url

    def _build_headers(self, api_endpoint, api_method):
        timestamp = self._create_timestamp()
        message = self._build_message(api_endpoint, api_method, timestamp)
        signature = self._build_signature(message)
        return {
            "TimeStamp": self._create_timestamp(),
            "Authorization": self._build_authentication_header(signature),
            "INTF-DatabaseID": self.config.database_id,
        }

    @staticmethod
    def _create_timestamp():
        return datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def _build_message(self, api_endpoint, api_method, timestamp):
        return f"{api_method}\n\n\n{timestamp}\n{api_endpoint}"

    def _build_signature(self, message):
        signature_bytes = hmac.new(
            self.config.private_key.encode(), message.encode(), hashlib.sha1
        ).digest()
        return base64.b64encode(signature_bytes).decode()

    def _build_authentication_header(self, signature):
        return f"INTF {self.config.public_key}:{signature}"
