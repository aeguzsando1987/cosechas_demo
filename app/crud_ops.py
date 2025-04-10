from sqlalchemy.orm import Session
from .models import Cuadrilla, Recolector, Tabla, Macrotunel, Cosecha
from .utils import cls_pantalla, espera, encoder_prueba
from .consultas import listar_cuadrillas, listar_recolectores

def agregar_cuadrilla(session:Session):
    print("\n" + "═"*65)
    print("NUEVA CUADRILLA".center(65))
    print("═"*65)
    
    try:
        responsable = input("│ Responsable a cargo: ").strip()
        localidad = input("│ Localidad de trabajo: ").strip()

        nueva_cuadrilla = Cuadrilla(
            responsable=responsable,
            localidad=localidad
        )

        session.add(nueva_cuadrilla)
        session.commit()
        session.refresh(nueva_cuadrilla)
        
        print("═"*65)
        print(f"[OK]: Cuadrilla registrada exitosamente!")
        print(f"│ ID asignado: {nueva_cuadrilla.id}")
        print(f"│ Clave generada: {nueva_cuadrilla.clave}")
        print("═"*65)

    except Exception as e:
        session.rollback()
        print(f"\n[ERROR] Error al registrar cuadrilla: {str(e)}")
        
def agregar_recolector(session:Session):
    print("\n" + "═"*65)
    print("NUEVO RECOLECTOR".center(65))
    print("═"*65)
    
    try:
        nombre_completo = input("│ Nombre completo: ").strip()
        localidad = input("│ Localidad de recolector: ").strip()
        tel = input("│ Telefono de recolector(OPCIONAL): ").strip()
        listar_cuadrillas(session)
        id_cuadrilla = int(input("│ Numero de cuadrilla: ").strip())
        nuevo_recolector = Recolector(
            nombre_completo = nombre_completo,
            encoder = encoder_prueba(),
            localidad = localidad,
            tel = tel,
            id_cuadrilla = id_cuadrilla
        )
        
        session.add(nuevo_recolector)
        session.commit()
        session.refresh(nuevo_recolector)
        
        cls_pantalla()
        print("═"*65)
        print(f"[OK]: Recolector registrado exitosamente!")
        print(f"│ ID asignado: {nuevo_recolector.id}")
        print(f"│ Clave generada: {nuevo_recolector.clave}")
        print(f"| Cuadrilla asiganada: {nuevo_recolector.id_cuadrilla} - {nuevo_recolector.cuadrilla.localidad}")
        print("═"*65)
        
    except Exception as e:
        session.rollback()
        print(f"[ERROR]:{str(e)}")
