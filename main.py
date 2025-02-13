from fastapi import FastAPI
from database import engine, Base
from routers import users, words  # Eliminamos 'game'

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir routers existentes
app.include_router(users.router, prefix="/api", tags=["usuarios"])
app.include_router(words.router, prefix="/api", tags=["palabras"])

@app.get("/")
def root():
    return {"message": "Bienvenido a El Penjat con FastAPI"}
