import os


class InterfolioConfig:
    @classmethod
    def get_or_raise(cls, variable, variable_name, env_variable_name):
        if variable is not None:
            return variable
        else:
            return cls.get_from_environment_or_raise(variable_name, env_variable_name)

    @staticmethod
    def get_raise_message(variable_name, env_variable_name):
        return f"'{variable_name}' must either be passed into the constructor or set as the environment variable '{env_variable_name}'"

    @classmethod
    def get_from_environment_or_raise(cls, variable_name, env_variable_name):
        if env_variable := os.environ.get(env_variable_name):
            return env_variable
        raise ValueError(cls.get_raise_message(variable_name, env_variable_name))


class InterfolioFARConfig(InterfolioConfig):
    def __init__(self, database_id=None, public_key=None, private_key=None):
        self.database_id = self.get_or_raise(
            database_id, "database_id", "FAR_DATABASE_ID"
        )
        self.public_key = self.get_or_raise(
            public_key, "public_key", "INTERFOLIO_PUBLIC_KEY"
        )
        self.private_key = self.get_or_raise(
            private_key, "private_key", "INTERFOLIO_PRIVATE_KEY"
        )
        self.host = "faculty180.interfolio.com/api.php"


class InterfolioFSConfig(InterfolioConfig):
    def __init__(self, tenant_id=None, public_key=None, private_key=None):
        self.tenant_id = self.get_or_raise(
            tenant_id, "tenant_id", "INTERFOLIO_TENANT_ID"
        )
        self.public_key = self.get_or_raise(
            public_key, "public_key", "INTERFOLIO_PUBLIC_KEY"
        )
        self.private_key = self.get_or_raise(
            private_key, "private_key", "INTERFOLIO_PRIVATE_KEY"
        )
        self.host = "logic.interfolio.com"


class InterfolioRPTConfig(InterfolioConfig):
    def __init__(self, tenant_id=None, public_key=None, private_key=None):
        self.tenant_id = self.get_or_raise(
            tenant_id, "tenant_id", "INTERFOLIO_TENANT_ID"
        )
        self.public_key = self.get_or_raise(
            public_key, "public_key", "INTERFOLIO_PUBLIC_KEY"
        )
        self.private_key = self.get_or_raise(
            private_key, "private_key", "INTERFOLIO_PRIVATE_KEY"
        )
        self.host = "logic.interfolio.com"


class InterfolioCoreConfig(InterfolioConfig):
    def __init__(self, tenant_id=None, public_key=None, private_key=None):
        self.tenant_id = self.get_or_raise(
            tenant_id, "tenant_id", "INTERFOLIO_TENANT_ID"
        )
        self.public_key = self.get_or_raise(
            public_key, "public_key", "INTERFOLIO_PUBLIC_KEY"
        )
        self.private_key = self.get_or_raise(
            private_key, "private_key", "INTERFOLIO_PRIVATE_KEY"
        )
        self.host = "logic.interfolio.com"
