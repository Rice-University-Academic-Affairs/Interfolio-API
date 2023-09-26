from .interfolio_config import InterfolioFSConfig
from .interfolio_core import InterfolioCore


class InterfolioFS(InterfolioCore):
    def __init__(self, tenant_id=None, public_key=None, private_key=None):
        super().__init__(
            InterfolioFSConfig(
                tenant_id=tenant_id, public_key=public_key, private_key=private_key
            )
        )

    def get_positions(self, **query_params):
        api_endpoint = f"/byc-search/{self.config.tenant_id}/positions"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)
