__all__ = ['LoginFailedException']


class LoginFailedException(Exception):
    """Raise when login failed"""

    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}
