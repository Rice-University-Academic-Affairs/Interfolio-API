import os
import pytest
from unittest import mock
from src.interfolio_api.interfolio_far_config import InterfolioFARConfig


class TestInterfolioFARConfig:
    @mock.patch.dict(os.environ, {"fake_variable": "fake_value"})
    def test__get_from_environment_or_raise(self):
        raise_message = "raise_message"
        assert (
            InterfolioFARConfig._get_from_environment_or_raise(
                "fake_variable", raise_message
            )
            == "fake_value"
        )

        with pytest.raises(ValueError, match=raise_message):
            InterfolioFARConfig._get_from_environment_or_raise(
                "missing_variable", raise_message
            )

    def test__get_database_id_from_provided(self):
        fake_id = "id"
        passed_in = InterfolioFARConfig(
            database_id=fake_id, public_key="key", private_key="key"
        )
        assert passed_in._get_database_id(fake_id) == fake_id

    @mock.patch.dict(os.environ, {"FAR_DATABASE_ID": "id"})
    def test__get_database_id_from_environment(self):
        from_env = InterfolioFARConfig(public_key="key", private_key="key")
        assert from_env._get_database_id(None) == "id"

    def test__get_database_id_missing(self):
        with pytest.raises(ValueError, match="`database_id` must either be passed.*"):
            missing = InterfolioFARConfig(public_key="key", private_key="key")

    def test__get_public_key_from_provided(self):
        fake_key = "fake_public_key"
        passed_in = InterfolioFARConfig(
            database_id="id", public_key=fake_key, private_key="key"
        )
        assert passed_in._get_public_key(fake_key) == fake_key

    @mock.patch.dict(os.environ, {"INTERFOLIO_PUBLIC_KEY": "fake_public_key"})
    def test__get_public_key_from_environment(self):
        from_env = InterfolioFARConfig(database_id="id", private_key="key")
        assert from_env._get_public_key(None) == "fake_public_key"

    def test__get_pubic_key_missing(self):
        with pytest.raises(ValueError, match="`public_key` must either be passed.*"):
            missing = InterfolioFARConfig(database_id="id", private_key="key")

    def test__get_private_key_from_provided(self):
        fake_key = "fake_private_key"
        passed_in = InterfolioFARConfig(
            database_id="id", public_key="key", private_key=fake_key
        )
        assert passed_in._get_private_key(fake_key) == fake_key

    @mock.patch.dict(os.environ, {"INTERFOLIO_PRIVATE_KEY": "fake_private_key"})
    def test__get_private_key_from_environment(self):
        from_env = InterfolioFARConfig(database_id="id", public_key="key")
        assert from_env._get_private_key(None) == "fake_private_key"

    def test__get_private_key_missing(self):
        with pytest.raises(ValueError, match="`private_key` must either be passed.*"):
            missing = InterfolioFARConfig(database_id="id", public_key="key")
