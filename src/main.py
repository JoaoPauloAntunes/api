from fastapi import (
  FastAPI,
)


backend = FastAPI()

@backend.get("/", tags=["Checker"])
async def rootil():
    import threading

    threads = threading.active_count()
    return {"message": "FRONTEND-MID-API", "threads": threads}