import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
import pyodbc
from app.config import Config

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={Config.DB_SERVER};"
    f"DATABASE={Config.DB_NAME};"
    f"UID={Config.DB_USER};"
    f"PWD={Config.DB_PASSWORD}"
)
print("¡Conexión exitosa!")
conn.close()