import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    DB_SERVER = os.getenv("DB_SERVER", "localhost\\SQLEXPRESS")
    DB_NAME = os.getenv("DB_NAME", "CosechaDB")
    DB_USER = os.getenv("DB_USER", "sa")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "TI.Sistemas.2025")
    
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )