from bot import run_bot
from api import app
import threading

def start_fastapi():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)

if __name__ == "__main__":
    # Inicia FastAPI en un thread
    threading.Thread(target=start_fastapi).start()

    # Inicia el bot en el hilo principal
    run_bot()
