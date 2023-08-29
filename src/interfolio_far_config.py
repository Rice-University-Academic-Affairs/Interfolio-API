import os


class InterfolioFARConfig:
    def __init__(self, database_id=None, public_key=None, private_key=None):
        self.database_id = self._get_database_id(database_id)
        self.public_key = self._get_public_key(public_key)
        self.private_key = self._get_private_key(private_key)
        self.host = "https://faculty180.interfolio.com/api.php"

    def _get_database_id(self, database_id):
        if database_id is not None:
            return database_id
        return self._get_from_environment_or_raise(
            "FAR_DATABASE_ID",
            "`database_id` must either be passed into InterfolioFARConfig or set as the environment variable "
            "'FAR_DATABASE_ID'",
        )

    def _get_public_key(self, public_key):
        if public_key is not None:
            return public_key
        return self._get_from_environment_or_raise(
            "FAR_PUBLIC_KEY",
            "`public_key` must either be passed into InterfolioFARConfig or set as the environment variable "
            "'FAR_PUBLIC_KEY'",
        )

    def _get_private_key(self, private_key):
        if private_key is not None:
            return private_key
        return self._get_from_environment_or_raise(
            "FAR_PRIVATE_KEY",
            "`private_key` must either be passed into InterfolioFARConfig or set as the environment variable "
            "'FAR_PRIVATE_KEY'",
        )

    @staticmethod
    def _get_from_environment_or_raise(env_variable_name, raise_message):
        if env_variable := os.environ.get(env_variable_name):
            return env_variable
        raise ValueError(raise_message)
