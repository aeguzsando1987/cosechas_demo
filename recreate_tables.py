import sys
from pathlib import Path
from sqlalchemy import create_engine, inspect
from app.config import Config
from app.database import Base  # Importar la Base para acceso a metadatos
from app.models import Cuadrilla, Recolector, Tabla, Macrotunel, Cosecha

sys.path.append(str(Path(__file__).parent))

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

def recrear_tablas():
    inspector = inspect(engine)
    
    try:
 
        print("\nEliminando tablas existentes...")
        Base.metadata.drop_all(engine)
        
        print("\nCreando tablas...")
        Base.metadata.create_all(engine)
        
        tablas_creadas = inspector.get_table_names()
        print("\nTablas creadas:", tablas_creadas)
        
        print("\n=== Estructura de Tablas ===")
        for tabla in tablas_creadas:
            print(f"\nTabla: {tabla}")
            columnas = inspector.get_columns(tabla)
            for col in columnas:
                print(f"- {col['name']} ({col['type']}, Nullable: {col['nullable']}")

    except Exception as e:
        print(f"\[ERROR]: {str(e)}")
        raise

if __name__ == "__main__":
    recrear_tablas()