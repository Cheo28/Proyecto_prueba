from fastapi import FastAPI
from routes.routes import router

app = FastAPI(title="Dashboard Modularizado")

# Incluir las rutas de la carpeta routes
app.include_router(router)