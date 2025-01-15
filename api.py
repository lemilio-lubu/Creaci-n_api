from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated
import operaciones_consulta 
from sqlmodel import Session
from modelo import get_db

app = FastAPI()

class ProductoCreate(BaseModel):
    nombre: str
    stock: int

@app.get("/producto/{id_producto}")
def leer_producto(id_producto: int, db: Session = Depends(get_db)):
    try:
        producto = operaciones_consulta.consultar_producto(id_producto, db)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return producto
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/producto/")
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    try:
        nuevo_producto = operaciones_consulta.agregar_producto(producto.nombre, producto.stock, db)
        return nuevo_producto
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/producto/{id_producto}")
def actualizar_producto(id_producto: int, stock: int, db: Session = Depends(get_db)):
    try:
        producto_actualizado = operaciones_consulta.actualizar_stock(id_producto, stock, db)
        if not producto_actualizado:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return producto_actualizado
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
