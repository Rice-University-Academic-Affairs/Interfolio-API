from .interfolio_config import InterfolioFSConfig
from .interfolio_base import InterfolioBase
from urllib.parse import urlencode


class InterfolioFS(InterfolioBase):
    def __init__(self, tenant_id=None, public_key=None, private_key=None):
        super().__init__(
            InterfolioFSConfig(
                tenant_id=tenant_id, public_key=public_key, private_key=private_key
            )
        )

    @staticmethod
    def _build_message(api_endpoint, api_method, timestamp, **query_params):
        api_endpoint = (
            f"{api_endpoint}?{urlencode(query_params)}"
            if query_params
            else api_endpoint
        )
        return f"{api_method}\n\n\n{timestamp}\n{api_endpoint}"

    def get_positions(self, **query_params):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_position(self, position_id, **query_params):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions/{position_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_position_types(self):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/position_types"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def create_position(self, payload):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions"
        api_method = "POST"
        return self._build_and_send_request(api_endpoint, api_method, payload=payload)

    def delete_position(self, position_id):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions/{position_id}"
        api_method = "DELETE"
        return self._build_and_send_request(api_endpoint, api_method)

    def create_position_type(self, name, category_id):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/position_types"
        api_method = "POST"
        return self._build_and_send_request(
            api_endpoint, api_method, payload={"name": name, "category_id": category_id}
        )

    def get_position_forms(self, position_id):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions/{position_id}/position_forms"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def get_applications(self, position_id):
        api_endpoint = (
            f"/byc-search/{self.config.tenant_id}/positions/{position_id}/applications"
        )
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def get_application(self, position_id, application_id):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions/{position_id}/applications/{application_id}/detail"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def create_application(self, position_id, payload):
        api_endpoint = (
            f"/byc-search/{self.config.tenant_id}/positions/{position_id}/applications"
        )
        api_method = "POST"
        return self._build_and_send_request(api_endpoint, api_method, payload=payload)

    def delete_application(self, position_id, application_id):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions/{position_id}/applications/{application_id}"
        api_method = "DELETE"
        return self._build_and_send_request(api_endpoint, api_method)

    def get_application_eeo(self, position_id, application_id):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions/{position_id}/applications/{application_id}/eeo_responses"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def create_application_eeo_responses(self, application_id, payload):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/byc_applications/{application_id}/responses/create_or_update_eeo"
        api_method = "PUT"
        return self._build_and_send_request(api_endpoint, api_method, payload=payload)

    def get_application_ratings(self, position_id, application_id):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions/{position_id}/applications/{application_id}/application_ratings"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def get_position_statuses(self, unit_id, status_type):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/units/{unit_id}/statuses/{status_type}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def create_application_attachment(
        self, 
        position_id,
        application_id, 
        display_name, 
        file_path,
    ):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions/{position_id}/byc_applications/{application_id}/application_attachments"
        api_method = "POST"
        
        # Create the form data
        data = {
            "attachment[display_name]": display_name,
        }
        
        # Open and send the PDF file
        with open(file_path, 'rb') as pdf_file:
            files = {
                'attachment[file]': pdf_file
            }
            
            return self._build_and_send_request(
                api_endpoint, 
                api_method, 
                form_data=data,
                files=files
            )