import pytest
import hmac
import hashlib
import base64
from src.interfolio_far import InterfolioFAR
from freezegun import freeze_time


@pytest.fixture
def far():
    return InterfolioFAR(
        database_id="id", public_key="public_key", private_key="private_key"
    )


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

    def test__build_signature(self, far):
        message = "message"
        signature_bytes = hmac.new(
            far.config.private_key.encode(), message.encode(), hashlib.sha1
        ).digest()
        signature = base64.b64encode(signature_bytes).decode()
        assert far._build_signature(message) == signature

    @freeze_time("1994-12-02 10:00:00")
    def test__create_timestamp(self):
        assert InterfolioFAR._create_timestamp() == "1994-12-02 10:00:00"

    def test__build_authentication_header(self, far):
        signature = "signature"
        assert (
            far._build_authentication_header(signature)
            == f"INTF {far.config.public_key}:{signature}"
        )
