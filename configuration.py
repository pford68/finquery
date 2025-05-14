import os
from dotenv import load_dotenv

load_dotenv()

try:
    os.environ["RDS_USER"]
except KeyError as e:
    print("Set the required environment variables. See the documentation for more details.")

'''Configuration class

Requires the following environment variables:
* RDS_USER
* RDS_PASSWORD
* RDS_HOST
* RDS_NAME

The following environment variables are optional:
* RDS_PORT:  defaults to 3306
'''
class Configuration:
    TYPE = os.getenv('RDS_TYPE')
    USER = os.getenv('RDS_USER')
    PASSWORD = os.getenv('RDS_PWD')
    HOST = os.getenv('RDS_HOST')
    PORT = os.getenv('RDS_PORT', 3306)
    DATABASE = os.getenv('RDS_DB_NAME')
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
