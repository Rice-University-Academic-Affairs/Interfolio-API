from .interfolio_config import InterfolioCoreConfig
from .interfolio_base import InterfolioBase


class InterfolioCore(InterfolioBase):
    def __init__(self, tenant_id=None, public_key=None, private_key=None):
        super().__init__(
            InterfolioCoreConfig(
                tenant_id=tenant_id, public_key=public_key, private_key=private_key
            )
        )

    def get_forms(self, service):
        """
        :param service: either 'search' or 'tenure'
        """
        api_endpoint = f"/byc/core/{service}/{self.config.tenant_id}/units/{self.config.tenant_id}/custom_forms"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def get_form(self, service, id):
        api_endpoint = (
            f"/byc/core/{service}/{self.config.tenant_id}/custom_forms/{int(id)}"
        )
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)
