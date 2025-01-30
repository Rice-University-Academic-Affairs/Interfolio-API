from .interfolio_config import InterfolioRPTConfig
from .interfolio_base import InterfolioBase
from urllib.parse import urlencode


class InterfolioRPT(InterfolioBase):
    def __init__(self, tenant_id=None, public_key=None, private_key=None):
        super().__init__(
            InterfolioRPTConfig(
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

    def get_packets(self, **query_params):
        api_endpoint = f"/byc-tenure/v2/{self.config.tenant_id}/packets"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)
