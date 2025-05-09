import os
from dotenv import load_dotenv

load_dotenv()

try:
    os.environ["FINQ_DB_USER"]
except KeyError as e:
    print("Set the required environment variables. See the documentation for more details.")

'''Configuration class

Requires the following environment variables:
* FINQ_DB_USER
* FINQ_DB_PASSWORD
* FINQ_DB_HOST
* FINQ_DB_NAME

The following environment variables are optional:
* FINQ_DB_PORT:  defaults to 3306
'''
class Configuration:
    TYPE = os.getenv('FINQ_DB_TYPE')
    USER = os.getenv('FINQ_DB_USER')
    PASSWORD = os.getenv('FINQ_DB_PWD')
    HOST = os.getenv('FINQ_DB_HOST')
    PORT = os.getenv('FINQ_DB_PORT', 3306)
    DATABASE = os.getenv('FINQ_DB_NAME')
    RAISE_ON_WARNINGS = True

    def __init__(self, **kwargs):
        self.RAISE_ON_WARNINGS = kwargs.get('RAISE_ON_WARNINGS', True)

    def params(self):
        return {
            'user': self.USER,
            'password': self.PASSWORD,
            'host': self.HOST,
            'port': self.PORT,
            'database': self.DATABASE,
            'raise_on_warnings': self.RAISE_ON_WARNINGS,
        }
