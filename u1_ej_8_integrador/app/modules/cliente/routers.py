from fastapi import APIRouter
from typing import List
from . import services
from .schemas import ClienteCreate, ClienteUpdate, ClienteResponse

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(nombre: str = None):
    return services.get_clientes(nombre)


@router.post("/", response_model=ClienteResponse, status_code=201)
def crear_cliente(cliente: ClienteCreate):
    return services.crear_cliente(cliente)


@router.put("/{cliente_id}", response_model=ClienteResponse)
def actualizar_cliente(cliente_id: int, cliente: ClienteUpdate):
    return services.actualizar_cliente(cliente_id, cliente)