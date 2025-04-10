from tabulate import tabulate
from sqlalchemy.orm import Session
from .models import Recolector, Cuadrilla, Tabla, Macrotunel, Cosecha
from .database import SessionLocal
from .utils import cls_pantalla, espera

def listar_cuadrillas(session: Session):
    cuadrillas = session.query(Cuadrilla).all()
    
    if not cuadrillas:
        print("\nNo hay cuadrillas registradas")
        return False
    
    datos = [[c.id, c.clave, c.responsable, c.localidad] for c in cuadrillas]
    headers = ["ID", "Clave", "Responsable", "Localidad"]
    
    print("\n" + "═"*65)
    print("CUADRILLAS REGISTRADAS".center(65))
    print("═"*65)
    print(tabulate(datos, headers=headers, tablefmt="pretty", numalign="center"))
    print("═"*65 + "\n")
    return True

def listar_recolectores(session: Session):
    recolectores = session.query(Recolector).all()
    
    if not recolectores:
        print("\nNo har recolectores registrados")
        return False
    
    datos = [[r.id, r.clave, r.nombre_completo] for r in recolectores]
    headers = ["ID", "Clave", "Nombre", "Localidad"]
    
    print("\n" + "═"*65)
    print("RECOLECTORES REGISTRADOS".center(65))
    print("═"*65)
    print(tabulate(datos, headers=headers, tablefmt="pretty", numalign="center"))
    print("═"*65 + "\n")
    return True


def consultar_recolectores(session: Session):
    print("\n" + "="*65)
    print("CONSULTA DE RECOLECTORES".center(65))
    print("="*65)
    
    try:
        nombre_busqueda = input("|  Ingrese un nombre para consultar: ").strip()
        cls_pantalla()
        
        recolectores = session.query(Recolector).join(Cuadrilla).filter(
            Recolector.nombre_completo.ilike(f"%{nombre_busqueda}%")
        )
        
        if not recolectores:
            
            print("No se encontraron recolectores con ese criterio")
            return
        
        datos = []
        for r in recolectores:
            datos.append([
                r.id,
                r.clave,
                r.nombre_completo,
                r.localidad,
                r.tel if r.tel else "N/A",
                f"{r.cuadrilla.clave} - {r.cuadrilla.localidad}"   
            ])
            
        headers = ["ID", "Clave", "Nombre", "Localidad", "Telefono", "Cuadrilla Asignada"]
        print("\n" + "═"*65)
        print("RESULTADOS DE BÚSQUEDA".center(65))
        print("═"*65)
        print(tabulate(datos, headers=headers, tablefmt="pretty", numalign="center"))
        print("═"*65 + "\n")
        
    except Exception as e:
        print(f"[ERROR]: {str(e)}")
    finally:
        input("\nPresione Enter para continuar...")
        cls_pantalla()
        
        
        