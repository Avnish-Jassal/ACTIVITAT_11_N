from sqlalchemy.orm import Session
import models, schemas

def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def get_palabras(db: Session):
    return db.query(models.Palabra).all()

def iniciar_partida(db: Session, usuario_id: int, palabra_id: int):
    partida = models.RegistroJuego(usuario_id=usuario_id, palabra_id=palabra_id)
    db.add(partida)
    db.commit()
    db.refresh(partida)
    return partida
