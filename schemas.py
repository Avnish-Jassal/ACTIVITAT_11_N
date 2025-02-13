from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

class PalabraBase(BaseModel):
    palabra: str

class PalabraResponse(PalabraBase):
    id: int

    class Config:
        orm_mode = True

class RegistroJuegoBase(BaseModel):
    usuario_id: int
    palabra_id: int

class RegistroJuegoResponse(RegistroJuegoBase):
    id: int
    intentos: int
    aciertos: str
    errores: int

    class Config:
        orm_mode = True
