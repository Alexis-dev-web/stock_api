import werkzeug.exceptions as ex


class ValueRequiredException(Exception):
    """
    Exception raised for values required.

    Attributes:
    ----------
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)