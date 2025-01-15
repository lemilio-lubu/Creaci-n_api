from typing import Generator
from sqlmodel import Field, Session, SQLModel, create_engine
from fastapi import FastAPI, HTTPException, Depends

# Model Producto
class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    stock: int

# Configuracion de la base de datos
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine, checkfirst=True)

# Obtener la instancia de la base de datos
def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session