from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    partidas = relationship("RegistroJuego", back_populates="jugador")

class Palabra(Base):
    __tablename__ = "palabras"
    id = Column(Integer, primary_key=True, index=True)
    palabra = Column(String, unique=True, index=True)

class RegistroJuego(Base):
    __tablename__ = "registro_juego"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    palabra_id = Column(Integer, ForeignKey("palabras.id"))
    intentos = Column(Integer, default=0)
    aciertos = Column(String, default="")
    errores = Column(Integer, default=0)
    jugador = relationship("Usuario", back_populates="partidas")
    palabra = relationship("Palabra")
