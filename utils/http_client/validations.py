from utils.http_client.api_exception import ApiException


def is_response_ok(res):
    """
    Check is response OK
    """
    if not res.ok:
        raise ApiException(res)
