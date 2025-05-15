import logging

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import traceback

from app.configuration import config as c


class Connection:
    """Wrapper for a database connection"""

    engine = None
    session = None

    def __init__(self):
        try:
            self.engine = create_engine(
                f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}:{c.PORT}/{c.DATABASE}",
                echo=True,  # Enable verbose logging for debugging
                pool_pre_ping=True  # Test connections before use
            )
            logging.info("Engine created successfully!")
        except Exception as e:
            logging.error("Failed to create engine:")
            logging.error(traceback.format_exc())

        try:
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            logging.info("Session factory and instance created!")
        except Exception as e:
            logging.error("Failed to create session:")
            logging.error(traceback.format_exc())

    def execute(self, query):
        try:
            result = self.session.execute(text(query))
            rows = result.fetchall()
            return rows
        except Exception as e:
            logging.error("Connection tests failed:")
            logging.error(traceback.format_exc())
            return None
        finally:
            self.session.close()
            logging.info("Session closed.")
