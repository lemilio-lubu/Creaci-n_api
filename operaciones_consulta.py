from sqlmodel import Session, select
from modelo import Producto  # Importa el modelo Producto desde donde esté definido
  # Dependencia para obtener la sesión de base de datos

# Parte 1: Programación Defensiva

from typing import Generator
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, HTTPException, Depends

# Configuracion de la base de datos
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine, checkfirst=True)

# Obtener la instancia de la base de datos
def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

# Funciones de operaciones

def consultar_producto(id_producto: int, db: Session):
    if id_producto <= 0:
        raise ValueError("El ID del producto debe ser un número entero positivo.")

    statement = select(Producto).where(Producto.id == id_producto)
    producto = db.exec(statement).first()
    if not producto:
        return None

    return {"id": producto.id, "nombre": producto.nombre, "stock": producto.stock}

def agregar_producto(nombre: str, stock: int, db: Session):
    if stock < 0:
        raise ValueError("El stock debe ser un número entero no negativo.")

    nuevo_producto = Producto(nombre=nombre, stock=stock)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return {"id": nuevo_producto.id, "nombre": nuevo_producto.nombre, "stock": nuevo_producto.stock}

def actualizar_stock(id_producto: int, nueva_cantidad: int, db: Session):
    if id_producto <= 0:
        raise ValueError("El ID del producto debe ser un número entero positivo.")
    if nueva_cantidad < 0:
        raise ValueError("La nueva cantidad debe ser un número entero no negativo.")

    statement = select(Producto).where(Producto.id == id_producto)
    producto = db.exec(statement).first()
    if not producto:
        return None

    producto.stock = nueva_cantidad
    db.commit()
    db.refresh(producto)

    return {"id": producto.id, "nombre": producto.nombre, "stock": producto.stock}