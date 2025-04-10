from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import Config

connection_string = (
    f"mssql+pyodbc://{Config.DB_USER}:{Config.DB_PASSWORD}@"
    f"{Config.DB_SERVER}/{Config.DB_NAME}?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "use_scope_identity=True" 
)

engine = create_engine(connection_string)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    
# Old implementation for connection tests
# metadata = MetaData()
# def create_tables():
#     metadata.create_all(engine)
