import os


basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+pymysql://root:root@localhost/e2isa'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'email-smtp.us-west-2.amazonaws.com"'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'AKIAJL5FE6U5YBP4FLBA'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'AteHIoJxzNZ7nnfsH3bT7C1Cw2QWmPNk4v/kxzj8Jkak'
    ADMINS = ['nirav.j05@gmail.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    POSTS_PER_PAGE = 25