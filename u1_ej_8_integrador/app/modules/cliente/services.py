from fastapi import HTTPException
from typing import List
from .schemas import ClienteCreate, ClienteUpdate, ClienteResponse

# "Base de datos" fake
clientes = []
id_counter = 1


def get_clientes(nombre: str = None) -> List[ClienteResponse]:
    if nombre:
        return [c for c in clientes if nombre.lower() in c["nombre"].lower()]
    return clientes


def crear_cliente(cliente: ClienteCreate) -> ClienteResponse:
    global id_counter

    # ❗ regla de negocio
    if cliente.edad < 18:
        raise HTTPException(status_code=400, detail="El cliente debe ser mayor de edad")

    nuevo_cliente = cliente.dict()
    nuevo_cliente["id"] = id_counter

    clientes.append(nuevo_cliente)
    id_counter += 1

    return nuevo_cliente


def actualizar_cliente(cliente_id: int, cliente: ClienteUpdate) -> ClienteResponse:
    for c in clientes:
        if c["id"] == cliente_id:

            # ❗ regla de negocio
            if cliente.edad is not None and cliente.edad < 18:
                raise HTTPException(status_code=400, detail="Debe ser mayor de edad")

            if cliente.nombre is not None:
                c["nombre"] = cliente.nombre
            if cliente.email is not None:
                c["email"] = cliente.email
            if cliente.edad is not None:
                c["edad"] = cliente.edad

            return c

    raise HTTPException(status_code=404, detail="Cliente no encontrado")