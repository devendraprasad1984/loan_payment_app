import secrets


class Utils():
    """utility functions object"""
    token_length = None


    def __init__(self, token_length=16):
        self.token_length = token_length


    def get_secret_key(self):
        return secrets.token_urlsafe(self.token_length)
