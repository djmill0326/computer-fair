import hashlib
import os


WTF_CSRF_ENABLED = True
SECRET_KEY = hashlib.sha1(os.urandom(64)).hexdigest()