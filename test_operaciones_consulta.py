
import pytest
from sqlmodel import Session, create_engine
from modelo import SQLModel, Producto, get_db
from operaciones_consulta import consultar_producto, agregar_producto, actualizar_stock

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

def test_agregar_producto(session):
    producto = agregar_producto("Producto Test", 10, session)
    assert producto["nombre"] == "Producto Test"
    assert producto["stock"] == 10

def test_consultar_producto(session):
    nuevo_producto = agregar_producto("Producto Test", 10, session)
    producto = consultar_producto(nuevo_producto["id"], session)
    assert producto["nombre"] == "Producto Test"
    assert producto["stock"] == 10

def test_actualizar_stock(session):
    nuevo_producto = agregar_producto("Producto Test", 10, session)
    producto_actualizado = actualizar_stock(nuevo_producto["id"], 20, session)
    assert producto_actualizado["stock"] == 20

def test_consultar_producto_no_existente(session):
    producto = consultar_producto(999, session)
    assert producto is None

def test_agregar_producto_stock_negativo(session):
    with pytest.raises(ValueError):
        agregar_producto("Producto Test", -10, session)

def test_actualizar_stock_negativo(session):
    nuevo_producto = agregar_producto("Producto Test", 10, session)
    with pytest.raises(ValueError):
        actualizar_stock(nuevo_producto["id"], -5, session)

def test_actualizar_producto_no_existente(session):
    producto_actualizado = actualizar_stock(999, 20, session)
    assert producto_actualizado is None