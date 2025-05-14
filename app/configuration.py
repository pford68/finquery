import os
import logging
from dotenv import load_dotenv

load_dotenv()

'''Configuration class

Requires the following environment variables:
* RDS_USER
* RDS_PASSWORD
* RDS_HOST
* RDS_DB_NAME
* API_KEY

The following environment variables are optional:
* RDS_PORT:  defaults to 3306
* LOGG_LEVEL: defaults to INFO
'''


class Configuration:
    TYPE = os.getenv('RDS_TYPE')
    USER = os.getenv('RDS_USER')
    PASSWORD = os.getenv('RDS_PWD')
    HOST = os.getenv('RDS_HOST')
    PORT = os.getenv('RDS_PORT', 3306)
    DATABASE = os.getenv('RDS_DB_NAME')
    API_KEY = os.getenv('API_KEY')
    RAISE_ON_WARNINGS = True
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    def __init__(self, **kwargs):
        self.RAISE_ON_WARNINGS = kwargs.get('RAISE_ON_WARNINGS', True)
        logging.basicConfig(level=self.LOG_LEVEL)

    def params(self):
        return {
            'user': self.USER,
            'password': self.PASSWORD,
            'host': self.HOST,
            'port': self.PORT,
            'database': self.DATABASE,
            'raise_on_warnings': self.RAISE_ON_WARNINGS,
        }


config = Configuration()
