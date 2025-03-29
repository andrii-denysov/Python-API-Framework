from utils.logger.log import logger as log

from utils.http_client.response import Response


class Request:
    """
    Class request builder
    :param method: requests HTTP method, requests.post, requests.get etc.
    :param base_uri: base URL for request (optional)
    :param: function which takes one parameter - requests Response object (optional)
    """

    def __init__(self, method, base_uri="", validate=None):
        self._method = method
        self._base_uri = base_uri
        self._validate = validate
        self._uri = None
        self._body = None
        self._headers = {}
        self._query_params = {}

    def uri(self, route):
        """
        Set URI for request. Sets self.base_uri if exists
        :param route: request URI route. Must start with http://hostname if no base_uri was set
        """
        self._uri = self._base_uri + route

    def body(self, body):
        """
        Set request body
        :param body: either Python JSON-serializable object or string
        """
        self._body = body

    def headers(self, **headers):
        """
        Add request headers. Each method call adds new headers
        """
        self._headers.update(headers)

    def query_params(self, **query_params):
        """Add request query params. Each method call adds new query params"""
        self._query_params.update(query_params)

    def auth_token(self, token):
        """Set Bearer Authorization token header"""
        self._headers["Authorization"] = "Bearer {}".format(token)

    def send(self, **extra_params):
        """
        Send request
        :param extra_params: extra kwargs request
        :return: Response object
        """
        res = self._method(self._uri, json=self._body, headers=self._headers, params=self._query_params, timeout=5,
                           **extra_params)
        log.debug("GET: %s", self._uri)
        log.debug("HEADERS: %s", self.__get_headers_debug())
        if self._validate:
            self._validate(res)
        return Response(res)

    def __get_headers_debug(self):
        if self._headers:
            debug_headers = {**self._headers, 'authorization': "******"}
            debug_headers.pop("password", None)
            return debug_headers
        return ''
