import asyncio
from fastapi import FastAPI
from api import app as fastapi_app  # tu FastAPI API con rutas ya definidas
from bot import start_bot_async     # tu función async para arrancar bot

app = fastapi_app  # Exportamos la variable global app para Render

@app.on_event("startup")
async def startup_event():
    # Lanzamos el bot como tarea concurrente sin bloquear
    asyncio.create_task(start_bot_async())
