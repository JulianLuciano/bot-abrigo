import threading
import asyncio
from api import app as fastapi_app
from bot import start_bot_async

def start_fastapi():
    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=start_fastapi, daemon=True).start()
    asyncio.run(start_bot_async())
