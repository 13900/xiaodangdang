from my_error.APIException import APIException

class ServerError(APIException):
    code = 500
    msg = "server is invallid"
    data = ''


class ClientTypeError(APIException):
    code = 400
    msg = "client is invallid"
    data = ''


class ParameterException(APIException):
    code = 403
    msg = 'invalid parameter'
    data = ''


class AuthFailed(APIException):
    code = 401
    msg = 'invalid parameter'
    data = ''


class ValError(APIException):
    code = 404
    msg = 'invalid parameter'
    data = ''

