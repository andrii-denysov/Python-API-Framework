import json

from utils.helpers.common_actions import CommonActions
from utils.logger.log import logger as log


class ApiException(Exception):
    """
    API exception
    :param response: Response object from requests lib
    """

    def __init__(self, response):
        log_failed_response(response)
        super().__init__("API request failed")


def log_failed_response(response):
    """
    Log errors with for failed response with request data
    :param response: requests.Response object
    """

    def prettify_body(body):
        if body is None:
            return body
        try:
            body = CommonActions.parse_json(body)
            body = json.dumps(body, indent=2)
        except json.JSONDecodeError:
            pass
        return body

    req_body = prettify_body(response.request.body)
    res_body = prettify_body(response.content)

    log.error("[API] Occurred an error when call the API request last")
    log.error("[API] Request - Path: '{}'".format(response.request.url))
    log.error("[API] Request - Method: '{}'".format(response.request.method))
    log.error("[API] Request - Body: '{}'".format(req_body))
    log.error("[API] Response - Status Code: '{0}' - '{1}'".format(response.status_code, response.reason))
    log.error("[API] Response - Body: '{}'".format(res_body))
