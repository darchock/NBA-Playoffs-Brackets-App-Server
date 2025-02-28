from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# MySQL URL format: "mysql+mysqlconnector://username:password@host:port/database_name"
# DATABASE_URL = "mysql+mysqlconnector://admin:rxrVkZzc7dwgi5JvMYer@database-nba-playoff-predictions-test-2025.cjsgac0qm87k.us-east-2.rds.amazonaws.com:3306/db_test_2025"
DATABASE_URL = "mysql+mysqlconnector://root:DarchAlonz96@localhost:3306/db_test_2025"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
Base = declarative_base()

# Function to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()