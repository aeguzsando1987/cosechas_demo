import sys
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.config import Config
from app.models import Cuadrilla, Recolector, Tabla, Macrotunel, Cosecha
import socket

# Configurar path
sys.path.append(str(Path(__file__).parent))

# Crear motor y sesión
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)
pc_name = socket.gethostname()

def main():
    try:

        
        # COSECHA
        cosecha = Cosecha(
            carrito = pc_name,
            id_recolector = 2,
            id_macrotunel = 2,
            categoria = "A",
            calificacion = 0.16,
        )  
        
        session.add(cosecha)
        session.commit()
        session.refresh(cosecha)

        cosecha_db = session.query(Cosecha).filter_by(id=cosecha.id).first()
        print(f"Cosecha registrada: {cosecha_db.id}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    main()