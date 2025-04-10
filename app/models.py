from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, LargeBinary, event, func, select, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# Modelo Cuadrilla
class Cuadrilla(Base):
    __tablename__ = "cuadrillas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    clave = Column(String(20), nullable=True)
    responsable = Column(String(50), nullable=False)
    localidad = Column(String(100), nullable=False)

    # Relación 1:N con Recolector
    recolectores = relationship("Recolector", back_populates="cuadrilla")

# Modelo Recolector
class Recolector(Base):
    __tablename__ = "recolectores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    clave = Column(String(20), nullable=True)
    nombre_completo = Column(String(100), nullable=False)
    encoder = Column(String(200), nullable=False)
    foto = Column(LargeBinary)
    localidad = Column(String(100))
    tel = Column(String(20))
    id_cuadrilla = Column(Integer, ForeignKey("cuadrillas.id"), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now)
    acceso = Column(Boolean, default=True)

    # Relaciones
    cuadrilla = relationship("Cuadrilla", back_populates="recolectores")
    cosechas = relationship("Cosecha", back_populates="recolector")  # Corregido a singular

# Modelo Tabla
class Tabla(Base):
    __tablename__ = "tablas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    clave = Column(String(20), nullable=True)
    ubicacion = Column(String(100), nullable=False)
    descripcion = Column(String(200))
    num_mt = Column(Integer, nullable=False)

    # Relación 1:N con Macrotunel
    macrotuneles = relationship("Macrotunel", back_populates="tabla")

# Modelo Macrotunel
class Macrotunel(Base):
    __tablename__ = "macrotuneles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    clave = Column(String(50), nullable=True)
    id_tabla = Column(Integer, ForeignKey("tablas.id"), nullable=False)
    descripcion = Column(String(200))
    num_pasillos = Column(Integer, nullable=False)

    # Relaciones
    tabla = relationship("Tabla", back_populates="macrotuneles")
    cosechas = relationship("Cosecha", back_populates="macrotunel")  # Corregido a plural

# Modelo Cosecha
class Cosecha(Base):
    __tablename__ = "cosechas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    carrito = Column(String(50), nullable=False)
    id_recolector = Column(Integer, ForeignKey("recolectores.id"), nullable=False)
    id_macrotunel = Column(Integer, ForeignKey("macrotuneles.id"), nullable=False)
    categoria = Column(
        String(1),
        CheckConstraint("categoria IN ('A', 'B', 'C')"),
        nullable=False
    )
    calificacion = Column(
        Float,
        CheckConstraint("calificacion IS NULL OR (calificacion BETWEEN 0 AND 1)"),
        nullable=True
    )
    peso = Column(Float,nullable=False)
    foto = Column(LargeBinary)
    fecha_transaccion = Column(DateTime, default=datetime.now)

    # Relaciones
    recolector = relationship("Recolector", back_populates="cosechas")
    macrotunel = relationship("Macrotunel", back_populates="cosechas")

    # Restricciones a nivel de tabla
    __table_args__ = (
        CheckConstraint("categoria IN ('A', 'B', 'C')", name="check_categoria"),
        CheckConstraint("(calificacion BETWEEN 0 AND 1) OR calificacion IS NULL", name="check_calificacion")
    )

# Event listeners para generación automática de claves
@event.listens_for(Cuadrilla, "after_insert")
def generar_clave_cuadrilla(mapper, connection, target):
    if target.clave is None:
        target.clave = f"CUA{target.id}"
        connection.execute(
            mapper.mapped_table.update()
            .where(mapper.mapped_table.c.id == target.id)
            .values(clave=target.clave)
        )

@event.listens_for(Recolector, "after_insert")
def generar_clave_recolector(mapper, connection, target):
    if target.clave is None:
        target.clave = f"REC{target.id}"
        connection.execute(
            mapper.mapped_table.update()
            .where(mapper.mapped_table.c.id == target.id)
            .values(clave=target.clave)
        )

@event.listens_for(Tabla, "before_insert")
def generar_clave_tabla(mapper, connection, target):
    if target.clave is None:
        next_id = connection.execute(
            select(func.coalesce(func.max(Tabla.id) + 1, 1))
            .select_from(Tabla)
        ).scalar()
        target.clave = f"TAB{next_id}"

@event.listens_for(Macrotunel, "before_insert")
def generar_clave_macrotunel(mapper, connection, target):
    if target.clave is None:
        next_id = connection.execute(
            select(func.coalesce(func.max(Macrotunel.id) + 1, 1))  # Corregido Macrotunel
            .select_from(Macrotunel)
        ).scalar()
        target.clave = f"MAC{next_id}"