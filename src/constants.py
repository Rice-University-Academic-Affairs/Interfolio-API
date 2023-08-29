from interfolio_far_config import InterfolioFARConfig

API_KEYS = {
    "public": "UB9J1J6L7M0KVWNAVZF60829PNI2VWMY",
    "private": "UAW9ZOFURHGOTNSR0MTV2IADYP4ZGC7ME5D6VORZG0IZNR260N5609J2TBRS7PYCMLMPID80X7JS7CRN60IEAIFHD8M0UUUZZPFU9C3LUGY6IHBF20IXH2SL647ESEU65M",
}

API_INFO = {
    "environment": {
        "prod": {"tenant_id": 41527, "database_id": "rice"},
        "dev": {"tenant_id": 46332, "database_id": "rice_dev"},
    },
    "host": "https://faculty180.interfolio.com/api.php",
}

dev_config = InterfolioFARConfig(
    database_id=API_INFO["environment"]["dev"]["database_id"],
    public_key=API_KEYS["public"],
    private_key=API_KEYS["private"],
)

prod_config = InterfolioFARConfig(
    database_id=API_INFO["environment"]["prod"]["database_id"],
    public_key=API_KEYS["public"],
    private_key=API_KEYS["private"],
)
