from base64 import b64encode


def get_authorization_header(auth_details):
    """ Generate Basic auth header """
    user, password = auth_details
    b64login = b64encode(bytes('%s:%s' % (user, password), "utf-8"))
    return b64login.decode('utf-8')


def create_header(auth_details=None, token=None):
    """ Returns headers """
    headers = {}
    if auth_details and auth_details is not None:
        code = get_authorization_header(auth_details)
        headers = {'Authorization': "Basic {code}".format(code=code)}
    elif token and token is not None:
        headers = {'token': token}
    headers['content-type'] = 'application/json'
    return headers






