import os
import pytest
from unittest import mock
from src.interfolio_api.interfolio_config import (
    InterfolioConfig,
    InterfolioFARConfig,
    InterfolioFSConfig,
    InterfolioRPTConfig,
)

FAR_DATABASE_ID = "FAR_DATABASE_ID"
PUBLIC_KEY = "INTERFOLIO_PUBLIC_KEY"
PRIVATE_KEY = "INTERFOLIO_PRIVATE_KEY"
TENANT_ID = "INTERFOLIO_TENANT_ID"


class TestInterfolioRPTConfig:
    def test_initialization(self):
        passed_in = InterfolioRPTConfig(TENANT_ID, PUBLIC_KEY, PRIVATE_KEY)
        assert passed_in.tenant_id == TENANT_ID
        assert passed_in.public_key == PUBLIC_KEY
        assert passed_in.private_key == PRIVATE_KEY
        assert passed_in.host == "logic.interfolio.com"

    def test_initialization_from_env(self):
        with mock.patch.dict(
            os.environ,
            {
                TENANT_ID: TENANT_ID,
                PUBLIC_KEY: PUBLIC_KEY,
                PRIVATE_KEY: PRIVATE_KEY,
            },
        ):
            from_env = InterfolioRPTConfig()
            assert from_env.tenant_id == TENANT_ID
            assert from_env.public_key == PUBLIC_KEY
            assert from_env.private_key == PRIVATE_KEY


class TestInterfolioFSConfig:
    def test_initialization(self):
        passed_in = InterfolioFSConfig(TENANT_ID, PUBLIC_KEY, PRIVATE_KEY)
        assert passed_in.tenant_id == TENANT_ID
        assert passed_in.public_key == PUBLIC_KEY
        assert passed_in.private_key == PRIVATE_KEY
        assert passed_in.host == "logic.interfolio.com"

    def test_initialization_from_env(self):
        with mock.patch.dict(
            os.environ,
            {
                TENANT_ID: TENANT_ID,
                PUBLIC_KEY: PUBLIC_KEY,
                PRIVATE_KEY: PRIVATE_KEY,
            },
        ):
            from_env = InterfolioFSConfig()
            assert from_env.tenant_id == TENANT_ID
            assert from_env.public_key == PUBLIC_KEY
            assert from_env.private_key == PRIVATE_KEY


class TestInterfolioFARConfig:
    def test_initialization(self):
        passed_in = InterfolioFARConfig(FAR_DATABASE_ID, PUBLIC_KEY, PRIVATE_KEY)
        assert passed_in.database_id == FAR_DATABASE_ID
        assert passed_in.public_key == PUBLIC_KEY
        assert passed_in.private_key == PRIVATE_KEY
        assert passed_in.host == "faculty180.interfolio.com/api.php"

    def test_intialization_from_env(self):
        with mock.patch.dict(
            os.environ,
            {
                FAR_DATABASE_ID: FAR_DATABASE_ID,
                PUBLIC_KEY: PUBLIC_KEY,
                PRIVATE_KEY: PRIVATE_KEY,
            },
        ):
            from_env = InterfolioFARConfig()
            assert from_env.database_id == FAR_DATABASE_ID
            assert from_env.public_key == PUBLIC_KEY
            assert from_env.private_key == PRIVATE_KEY


class TestInterfolioConfig:
    def test_get_or_raise(self):
        good_variable = "good_variable"
        assert (
            InterfolioConfig.get_or_raise(
                good_variable, "good_variable", "good_variable"
            )
            == good_variable
        )

        missing_variable = None
        with pytest.raises(ValueError, match=r".* must either be.*"):
            InterfolioConfig.get_or_raise(
                missing_variable, "missing_variable", "missing_variable"
            )

        environment_variable = "environment_variable"
        with mock.patch.dict(os.environ, {environment_variable: environment_variable}):
            assert (
                InterfolioConfig.get_or_raise(
                    None, environment_variable, environment_variable
                )
                == environment_variable
            )

    def test_get_raise_message(self):
        variable_name = "variable_name"
        env_variable_name = "env_variable_name"
        assert (
            InterfolioConfig.get_raise_message(variable_name, env_variable_name)
            == "'variable_name' must either be passed into the constructor or set as the environment variable 'env_variable_name'"
        )

    @mock.patch.dict(os.environ, {"fake_variable": "fake_value"})
    def test_get_from_environment_or_raise(self):
        assert (
            InterfolioConfig.get_from_environment_or_raise(
                "fake_variable", "fake_variable"
            )
            == "fake_value"
        )

        with pytest.raises(ValueError, match=r".* must either be.*"):
            InterfolioFARConfig.get_from_environment_or_raise(
                "missing_variable", "missing_variable"
            )
