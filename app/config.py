import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://bospacvdnhmblk:c464c9708b3eaebfdeb6cddf114c0938a1e8af06e14c00a75e63b98abbcf1d85@ec2-34-224-226-38.compute-1.amazonaws.com:5432/dbst7r3ekuid7m') or 'postgresql://project:nigga102@192.168.1.8:5433/project1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER=".uploads/"


#testing
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False