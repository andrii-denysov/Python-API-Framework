import json

from utils.http_client.assert_response import AssertResponse


class Response:
    """
    Response wrapper with assertions bindings
    """

    def __init__(self, response_obj):
        self._response = response_obj
        self._assert = AssertResponse(response_obj)

    @property
    def content(self):
        return json.loads(str(self._response._content, "utf-8"))

    @property
    def token_content(self):
        return str(self._response._content, "utf-8")

    @property
    def has(self):
        """
        Method to check if parameter in response has passed value
        """
        return self._assert

    @property
    def schema_validate(self):
        """
        Method to validate response schema
        """
        return self._assert.validate_schema
