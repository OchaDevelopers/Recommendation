#################################################
#   Exceptions relate to API Request            #
#################################################


class UnauthorizedException(Exception):
    def __init__(self, msg='API Authorizing Failed.'):
        super().__init__(msg)

class RequestGetException(Exception):
    def __init__(self, msg='API Requesting(Get) Failed.'):
        super().__init__(msg)

class RequestPostException(Exception):
    def __init__(self, msg='API Requesting(Post) Failed.'):
        super().__init__(msg)


#################################################
#   Exceptions etc.                             #
#################################################


class InvalidParameterException(Exception):
    def __init__(self, msg=''):
        super().__init__(msg)