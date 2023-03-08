import os
from os import getenv

pguser = getenv('pguser')
pgpassword = getenv('pgpassword')


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{pguser}:{pgpassword}@localhost:5432/study_hard"
    SECRET_KEY = os.urandom(24)
    
    # SECURITY_PASSWORD_SALT = 'salt'
    # SECURITY_PASSWORD_HASH = "bcrypt"

