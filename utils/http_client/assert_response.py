from functools import wraps

import json

from hamcrest import assert_that, equal_to, contains_string
from jsonschema import validate

from utils.http_client.api_exception import log_failed_response


def track_error(func):
    """
    Catch AssertionError, log request/response data and throw original AssertionError higher
    Works for methods of AssertResponse or JsonPathMatch only
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        instance = args[0]
        try:
            return func(*args, **kwargs)
        except AssertionError as ae:
            instance.log_request_response_data()
            raise ae

    return wrapper


class AssertResponse:
    """
    Object for common response assertions
    :param response_obj: Response object from requests lib
    """

    def __init__(self, response_obj):
        self._response = response_obj

    def log_request_response_data(self):
        """Logs request/response data as a failure"""
        log_failed_response(self._response)

    @track_error
    def status(self, exp_status):
        """
        Assert response status code
        :param exp_status: expected status code (int)
        """
        assert_that(exp_status, equal_to(self._response.status_code), "Status code is incorrect")

    @track_error
    def parameter(self, parameter, value, equals=False):
        """
        Assert that response body contains parameter with value
        :param equals: check if parameter value equals to expected
        :param value: expected parameter value
        :param parameter: parameter to be checked
        """
        if equals:
            assert_that(value, equal_to(self._response.json().get(parameter)),
                        "Body's parameter doesn't equal expected value")
        else:
            assert_that(value, contains_string(self._response.json().get(parameter)),
                        "Body's parameter doesn't contain expected value")

    @track_error
    def validate_schema(self, schema):
        """
        Assert that response has valid schema
        :param schema: schema from the swagger file
        """
        validate(instance=json.loads(self._response.content), schema=schema)
