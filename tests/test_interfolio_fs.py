from urllib.parse import urlencode

from conftest import assert_request_made_with_correct_arguments


class TestInterfolioFS:
    def test__build_message(self, fs):
        assert (
            fs._build_message("/endpoint", "GET", "timestamp", param="value")
            == "GET\n\n\ntimestamp\n/endpoint?param=value"
        )
        assert (
            fs._build_message("/endpoint", "GET", "timestamp")
            == "GET\n\n\ntimestamp\n/endpoint"
        )

    def test_get_positions(self, fs):
        api_endpoint = f"/byc-search/{fs.config.tenant_id}/positions"
        api_method = "GET"
        query_params = {"archived": "true"}
        assert_request_made_with_correct_arguments(
            fs, "get_positions", api_endpoint, api_method, **query_params
        )

    def test_get_position(self, fs):
        position_id = "position_id"
        api_endpoint = f"/byc-search/{fs.config.tenant_id}/positions/{position_id}"
        api_method = "GET"
        assert_request_made_with_correct_arguments(
            fs, "get_position", api_endpoint, api_method, position_id
        )

    def test_get_position_types(self, fs):
        api_endpoint = f"/byc-search/{fs.config.tenant_id}/position_types"
        api_method = "GET"
        assert_request_made_with_correct_arguments(
            fs,
            "get_position_types",
            api_endpoint,
            api_method,
        )

    def test_get_applications(self, fs):
        position_id = "position_id"
        api_endpoint = (
            f"/byc-search/{fs.config.tenant_id}/positions/{position_id}/applications"
        )
        api_method = "GET"
        assert_request_made_with_correct_arguments(
            fs,
            "get_applications",
            api_endpoint,
            api_method,
            position_id,
        )

    def test_get_application(self, fs):
        position_id = "position_id"
        application_id = "application_id"
        api_endpoint = f"/byc-search/{fs.config.tenant_id}/positions/{position_id}/applications/{application_id}/detail"
        api_method = "GET"
        assert_request_made_with_correct_arguments(
            fs,
            "get_application",
            api_endpoint,
            api_method,
            position_id,
            application_id,
        )

    def test_get_application_eeo(self, fs):
        position_id = "position_id"
        application_id = "application_id"
        api_endpoint = f"/byc-search/{fs.config.tenant_id}/positions/{position_id}/applications/{application_id}/eeo_responses"
        api_method = "GET"
        assert_request_made_with_correct_arguments(
            fs,
            "get_application_eeo",
            api_endpoint,
            api_method,
            position_id,
            application_id,
        )

    def test_get_application_ratings(self, fs):
        position_id = "position_id"
        application_id = "application_id"
        api_endpoint = f"/byc-search/{fs.config.tenant_id}/positions/{position_id}/applications/{application_id}/application_ratings"
        api_method = "GET"
        assert_request_made_with_correct_arguments(
            fs,
            "get_application_ratings",
            api_endpoint,
            api_method,
            position_id,
            application_id,
        )
