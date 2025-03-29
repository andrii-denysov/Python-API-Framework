import requests

from utils.http_client.request import Request
from utils.http_client.validations import is_response_ok

class HttpClient:
    """
    Http Client provides access to requests objects, pre-defines base URI and default token if set
    """

    __validate__ = None

    def __init__(self, base_uri="", default_token=None):
        self._base_uri = base_uri
        self._default_token = default_token

    def _prepare_request(self, method):
        """
        Prepare request object with given method and pre-defined data
        :param method: requests HTTP method, requests.post, requests.get etc.
        :return: instance of Request
        """
        request_ = Request(method, base_uri=self._base_uri, validate=self.__validate__)
        if self._default_token:
            request_.auth_token(self._default_token)
        return request_

    def post(self):
        """Return POST Request"""
        return self._prepare_request(requests.post)

    def get(self):
        """Return GET Request"""
        return self._prepare_request(requests.get)

    def patch(self):
        """Return PATCH Request"""
        return self._prepare_request(requests.patch)

    def put(self):
        """Return PUT request"""
        return self._prepare_request(requests.put)

    def delete(self):
        """Return DELETE request"""
        return self._prepare_request(requests.delete)


class HttpClientValidate(HttpClient):
    """Http client with validation that response status is OK"""

    __validate__ = is_response_ok
