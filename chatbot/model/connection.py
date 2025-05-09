import logging
import time
import mysql.connector

from configuration import Configuration

config = Configuration()

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to a file
file_handler = logging.FileHandler("db_errors.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class BaseConnection:
    _conn = None

    def connect(self, attempts=3, delay=2):
        attempt = 1
        # Implement a reconnection routine
        while attempt < attempts + 1:
            try:
                self._conn = self.get_connection()
                break
            except (self.get_exception_type(), IOError) as err:
                print("Exception")
                if attempt > attempts:
                    # Attempts to reconnect failed; returning None
                    logger.info("Failed to connect, exiting without a connection: %s", err)
                    return None
                logger.info(
                    "Connection failed: %s. Retrying (%d/%d)...",
                    err,
                    attempt,
                    attempts-1,
                )
                # progressive reconnect delay
                time.sleep(delay ** attempt)
                attempt += 1
        return self

    def close(self ):
        self._conn.close()

    def get_connection(self, **kwargs):
         # Implement in subclasses
         raise Exception("This method is abstract.")

    def get_exception_type(self):
        # Implement in subclasses
        raise Exception("This method is abstract")

    def cursor(self):
        return self._conn.cursor()


class MysqlConnection(BaseConnection):
    def get_connection(self):
        if self._conn is not None:
            return self._conn
        return mysql.connector.connect(**config.params())

    def get_exception_type(self):
        return mysql.connector.Error

class PostgresConnection(BaseConnection):
    def get_connection(self):
        raise Exception("Not implemented")

    def get_exception_type(self):
        raise Exception("Not implemented")


def connect(**kwargs):
    types = {
        'mysql': MysqlConnection,
        'postgres': PostgresConnection,
    }
    try:
        return types[config.TYPE]().connect(**kwargs)
    except KeyError:
        logger.error("Unknown connection type: %s", config.TYPE)
        return None

c = connect()
cursor = c.cursor()
cursor.execute("select * from transactions limit 10")
print(cursor.fetchall())

if (c is not None):
    c.close()


