import asyncio
from fastapi import FastAPI
from api import app as fastapi_app
from bot import start_bot_async

app = fastapi_app  # este es el que Render expone

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_bot_async())
