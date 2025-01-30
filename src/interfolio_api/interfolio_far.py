from .interfolio_config import InterfolioFARConfig
from .interfolio_base import InterfolioBase


class InterfolioFAR(InterfolioBase):
    def __init__(self, database_id=None, public_key=None, private_key=None):
        super().__init__(
            InterfolioFARConfig(
                database_id=database_id, public_key=public_key, private_key=private_key
            )
        )

    def get_units(self, **query_params):
        api_endpoint = "/units"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_unit(self, unit_id, **query_params):
        api_endpoint = f"/units/{unit_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_terms(self, **query_params):
        api_endpoint = "/terms"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_users(self, **query_params):
        api_endpoint = "/users"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_user(self, user_id, **query_params):
        api_endpoint = f"/users/{user_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_user_data(self, **query_params):
        api_endpoint = "/userdata"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_tenant_ids(self):
        api_endpoint = "/users/current"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method)

    def get_permissions(self, **query_params):
        api_endpoint = "/users/permissions"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_permission(self, user_id, **query_params):
        api_endpoint = f"/users/{user_id}/permissions"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_faculty_classification_data(self, **query_params):
        api_endpoint = "/facultyclassificationdata"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_faculty_classifications(self, **query_params):
        api_endpoint = "/facultyclassifications"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_faculty_classification(self, faculty_classification_id, **query_params):
        api_endpoint = f"/facultyclassifications/{faculty_classification_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_sections(self, **query_params):
        api_endpoint = "/sections"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_section(self, section_id, **query_params):
        api_endpoint = f"/sections/{section_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activities_ids_in_sections(self, **query_params):
        api_endpoint = "/activities"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activities_ids_for_section(self, section_id, **query_params):
        api_endpoint = f"/activities/{section_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activities_details_for_section(self, section_id, **query_params):
        api_endpoint = f"/activities_details/{section_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activity_details(self, section_id, activity_id, **query_params):
        api_endpoint = f"/activities/{section_id}/{activity_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activity_attachments(self, section_id, activity_id, **query_params):
        api_endpoint = f"/activities/{section_id}/{activity_id}/attachments"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activity_classifications(self, **query_params):
        api_endpoint = "/activityclassifications"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_activity_classification(self, activity_classification_id, **query_params):
        api_endpoint = f"/activityclassifications/{activity_classification_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_course_prefixes(self, **query_params):
        api_endpoint = "/courseprefixes"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_courses(self, **query_params):
        api_endpoint = "/courses"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_courses_taught(self, **query_params):
        api_endpoint = "/coursestaught"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_course_taught(self, course_taught_id, **query_params):
        api_endpoint = f"/coursestaught/{course_taught_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_course_taught_attachments(self, course_taught_id, **query_params):
        api_endpoint = f"/coursestaught/{course_taught_id}/attachments"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_evaluations(self, **query_params):
        api_endpoint = "/evaluations"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_vitae(self, **query_params):
        api_endpoint = "/vitas"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_vita(self, user_id, vita_id, **query_params):
        api_endpoint = f"/vitas/{vita_id}/{user_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def get_paginated_vitae(self, tenant_id, **query_params):
        api_endpoint = f"/{tenant_id}/vita_templates"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)

    def download_attachment(self, attachment_id, **query_params):
        api_endpoint = f"/downloadattachments/{attachment_id}"
        api_method = "GET"
        return self._build_and_send_request(api_endpoint, api_method, **query_params)
