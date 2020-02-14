# Create dummy secrey key so we can use sessions
SECRET_KEY = '456mo45i6o4ij5'

# Create in-memory database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:pass@localhost:3306/database'
SQLALCHEMY_ECHO = True

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "mk546mo54m6oi54m6o5i"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# altri settaggi
FLASK_ADMIN_SWATCH = 'cerulean'
CSRF_ENABLED = True
USER_ENABLE_EMAIL = True