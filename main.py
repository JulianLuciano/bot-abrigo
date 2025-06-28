import threading
import uvicorn
from fastapi import FastAPI
from api import router as api_router
from bot import run_bot  # esta función la vas a crear ahora

app = FastAPI()

# Incluir endpoints de API
app.include_router(api_router)

# Función para iniciar el bot en segundo plano
def start_bot():
    run_bot()

# Al levantar la app, también se inicia el bot
@app.on_event("startup")
def startup_event():
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()

