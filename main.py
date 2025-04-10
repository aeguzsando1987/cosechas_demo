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
from app.crud_ops import agregar_cuadrilla, agregar_recolector

sys.path.append(str(Path(__file__).parent))

from app.consultas import consultar_recolectores
from app.database import SessionLocal

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)
    



def menu_principal():
    print("     REGISTRO DE COSECHAS (DEMO V. a0.1.0)")
    print("="*40)
    print("Elija una opción:")
    print("[1] ADMINISTRAR PERSONAL")
    print("[2] ADMINISTRACION TABLAS")
    print("[2] COSECHAS")
    print("[0] Salir")
    print("="*40)
    
def menu_personal():
    try:
        print("     REGISTRO DE PERSONAL")
        print("="*40)
        print("Elija una opción:")
        print("[1] Registrar Cuadrilla")
        print("[2] Registrar Recolector")
        print("[3] Consultar recolectores")
        print("[4] Listar cuadrillas disponibles")
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

    except KeyboardInterrupt:
        print("Operación cancelada por usuario")
    finally:
        session.close()    
    



# def agregar_cuadrilla():
#     print("\n" + "═"*65)
#     print("NUEVA CUADRILLA".center(65))
#     print("═"*65)
    
#     try:
#         responsable = input("│ Responsable a cargo: ").strip()
#         localidad = input("│ Localidad de trabajo: ").strip()

#         nueva_cuadrilla = Cuadrilla(
#             responsable=responsable,
#             localidad=localidad
#         )

#         session.add(nueva_cuadrilla)
#         session.commit()
#         session.refresh(nueva_cuadrilla)
        
#         print("═"*65)
#         print(f"[OK]: Cuadrilla registrada exitosamente!")
#         print(f"│ ID asignado: {nueva_cuadrilla.id}")
#         print(f"│ Clave generada: {nueva_cuadrilla.clave}")
#         print("═"*65)

#     except Exception as e:
#         session.rollback()
#         print(f"\n[ERROR] Error al registrar cuadrilla: {str(e)}")
        
    
# def agregar_recolector():
#     print("\n" + "═"*65)
#     print("NUEVO RECOLECTOR".center(65))
#     print("═"*65)
    
#     try:
#         nombre_completo = input("│ Nombre completo: ").strip()
#         localidad = input("│ Localidad de recolector: ").strip()
#         tel = input("│ Telefono de recolector(OPCIONAL): ").strip()
#         listar_cuadrillas(session)
#         id_cuadrilla = int(input("│ Numero de cuadrilla: ").strip())
#         nuevo_recolector = Recolector(
#             nombre_completo = nombre_completo,
#             encoder = encoder_prueba(),
#             localidad = localidad,
#             tel = tel,
#             id_cuadrilla = id_cuadrilla
#         )
        
#         session.add(nuevo_recolector)
#         session.commit()
#         session.refresh(nuevo_recolector)
        
#         cls_pantalla()
#         print("═"*65)
#         print(f"[OK]: Recolector registrado exitosamente!")
#         print(f"│ ID asignado: {nuevo_recolector.id}")
#         print(f"│ Clave generada: {nuevo_recolector.clave}")
#         print(f"| Cuadrilla asiganada: {nuevo_recolector.id_cuadrilla} - {nuevo_recolector.cuadrilla.localidad}")
#         print("═"*65)
        
#     except Exception as e:
#         session.rollback()
#         print(f"[ERROR]:{str(e)}")


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