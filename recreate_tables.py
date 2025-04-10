import sys
from pathlib import Path
from sqlalchemy import create_engine, inspect
from app.config import Config
from app.database import Base  # Importar la Base para acceso a metadatos
from app.models import Cuadrilla, Recolector, Tabla, Macrotunel, Cosecha

# Configurar path
sys.path.append(str(Path(__file__).parent))

# Crear motor
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

def recrear_tablas():
    inspector = inspect(engine)
    
    try:
        # 1. Eliminar tablas existentes
        print("\nEliminando tablas existentes...")
        Base.metadata.drop_all(engine)
        
        # 2. Crear todas las tablas desde modelos
        print("\nCreando tablas...")
        Base.metadata.create_all(engine)
        
        # 3. Verificar tablas creadas
        tablas_creadas = inspector.get_table_names()
        print("\nTablas creadas:", tablas_creadas)
        
        # 4. Verificar estructura de todas las tablas
        print("\n=== Estructura de Tablas ===")
        for tabla in tablas_creadas:
            print(f"\nTabla: {tabla}")
            columnas = inspector.get_columns(tabla)
            for col in columnas:
                print(f"- {col['name']} ({col['type']}, Nullable: {col['nullable']}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    recrear_tablas()