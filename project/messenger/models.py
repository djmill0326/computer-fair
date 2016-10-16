from passlib.hash import sha256_crypt

class User():
    def __init__(self, username):
        self.username = username
        self.id = username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def get_user(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return sha256_crypt.verify(password, password_hash)
