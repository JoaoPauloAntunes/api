import uvicorn

if __name__ == "__main__":
  uvicorn.run("src.main:backend", reload=True, port=5001, host="0.0.0.0")