from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import traceback

from configuration import Configuration

config = Configuration()

# Create SQLAlchemy engine
try:
    engine = create_engine(
        f"mysql+mysqlconnector://{config.USER}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.DATABASE}",
        echo=True,  # Enable verbose logging for debugging
        pool_pre_ping=True  # Test connections before use
    )
    print("Engine created successfully!")
except Exception as e:
    print("Failed to create engine:")
    print(traceback.format_exc())

# Configure session factory
try:
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Session factory and instance created!")
except Exception as e:
    print("Failed to create session:")
    print(traceback.format_exc())


# Test connection via session
try:
    result = session.execute(text("SELECT * from transactions limit 10")).fetchall()
    print("Session connection to RDS established successfully!")
    print(f"Test query result: {result}")  # Should print [(1,)]
except Exception as e:
    print("Connection test failed:")
    print(traceback.format_exc())
finally:
    session.close()
    print("Session closed.")

# # List databases
# try:
#     dbs = pd.read_sql(text("SHOW DATABASES"), session.bind)
#     print("Databases:", dbs)
#     assert RDS_DB_NAME in dbs['Database'].values, f"{RDS_DB_NAME} not found!"
# except Exception as e:
#     print("Database check failed:", e)
# finally:
#     session.close()