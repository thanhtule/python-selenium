from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

# Firefox setting
FIREFOX_BINARY = config('FIREFOX_BINARY', default='')

# Default driver
DEFAULT_DRIVER = config('DEFAULT_DRIVER', default='FIREFOX')

# File path
ENVIRONMENT_PATH = config('ENVIRONMENT_PATH', default='release')
