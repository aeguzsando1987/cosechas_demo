import sys
from pathlib import Path
from datetime import datetime
from tabulate import tabulate
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.config import Config
from app.models import Cuadrilla, Recolector
from app.utils import cls_pantalla, espera, encoder_prueba
from app.consultas import listar_cuadrillas, listar_recolectores
from app.crud_ops import agregar_cuadrilla, agregar_recolector, actualizar_cuadrilla

sys.path.append(str(Path(__file__).parent))

from app.consultas import consultar_recolectores
from app.database import SessionLocal

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)
    



def menu_principal():
    print("     REGISTRO DE COSECHAS")
    print("="*40)
    print("Elija una opción:")
    print("[1] ADMINISTRAR PERSONAL")
    print("[2] ADMINISTRACION TABLAS")
    print("[2] COSECHAS")
    print("[0] Salir")
    print("="*40)
    
def menu_personal():
    try:
        print("REGISTRO DE PERSONAL".center(40))
        print("="*40)
        print("Elija una opción:")
        print("[1] Registrar Cuadrilla")
        print("[2] Registrar Recolector")
        print("[3] Consultar recolectores")
        print("[4] Listar cuadrillas disponibles")
        print("[5] Actualizar cuadrillas")
        print("="*40)
        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == "1":
            cls_pantalla()
            agregar_cuadrilla(session)

        elif opcion == "2":
            cls_pantalla()
            listar_cuadrillas(session)
            agregar_recolector(session)
            
        elif opcion == "3":
            consultar_recolectores(session)
            
        elif opcion == "4":
            cls_pantalla()
            listar_cuadrillas(session)
            
        elif opcion == "5":
            cls_pantalla()
            actualizar_cuadrilla(session)

    except KeyboardInterrupt:
        print("Operación cancelada por usuario")
    finally:
        session.close()
        
        

    
def main():
    try:
        while True:
            menu_principal()
            opcion = input("\n Seleccione una opción... ").strip()
            if opcion == "1":
                cls_pantalla()
                espera()
                menu_personal()
            elif opcion == "2":
                print("hola mundo 2")
                cls_pantalla()
            elif opcion == "0":
                print("BYE BYE")
                cls_pantalla()
                break
            else:
                cls_pantalla()
                print("Opción invalida")
            
            
    except KeyboardInterrupt:
        print("Operación cancelada por usuario")
    finally:
        session.close()
        
        
if __name__ == "__main__":
    main()