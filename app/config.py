import os

basedir = os.path.abspath(os.path.dirname(__file__))


# load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                          'postgres://postgres:postgres@localhost:5433/E2ISA'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+pymysql://root:root@localhost/e2isa'
    RECORDS_PER_PAGE = 4
    OAUTHLIB_INSECURE_TRANSPORT = 1
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
    OAUTH_CREDENTIALS_GOOGLE_ID ='33511635428-s6l2u5vicfqnd91c8sim6e1ktsdcgm3u.apps.googleusercontent.com'
    OAUTH_CREDENTIALS_GOOGLE_SECRET = 'eqSfdnNgBLOr4OJzH9OXdGoo'
    AUTHORISATION_BASE_URL = "https://accounts.google.com/o/oauth2/auth"
    TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
    refresh_url = TOKEN_URL  # True for Google but not all providers.
    SCOPE = ['profile', 'email']
    REDIRECT_URI = 'http://127.0.0.1:5000/callback'

    '''
    OAUTH_CREDENTIALS = {
        'Google': {
            'id': '33511635428-s6l2u5vicfqnd91c8sim6e1ktsdcgm3u.apps.googleusercontent.com',
            'secret': 'eqSfdnNgBLOr4OJzH9OXdGoo'
        }
        'twitter': {
            'id': 'R0qItN9CYMW3YYZXPq39rRMvh',
            'secret': 'RnPLRYzZOTB0yXFWjkVvlgaJf3qPkBkMpS949bC6WtKYMpXrVF'
        },
        'github': {
            'id': '3RzWQclolxWZIMq5LJqzRZPTl',
            'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
        }
    }
    '''
