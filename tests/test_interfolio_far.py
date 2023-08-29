import pytest
from src.interfolio_far import InterfolioFAR
from constants import API_KEYS
from freezegun import freeze_time


class TestInterfolioFAR:
    def test_initialization(self):
        public_key = "fake_pubic_key"
        private_key = "fake_private_key"
        database_id = "fake_database_id"
        far_api = InterfolioFAR(
            database_id=database_id, public_key=public_key, private_key=private_key
        )
        assert far_api.config.public_key == public_key
        assert far_api.config.private_key == private_key
        assert far_api.config.database_id == database_id

    @freeze_time("1994-12-02 10:00:00")
    def test__create_timestamp(self):
        assert InterfolioFAR._create_timestamp() == "1994-12-02 10:00:00"
