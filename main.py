import asyncio
from fastapi import FastAPI
from api import app as fastapi_app
from bot import start_bot_async

app = fastapi_app  # esto es lo que Render importa

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_bot_async())
