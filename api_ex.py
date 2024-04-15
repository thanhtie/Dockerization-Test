from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def central_function():
    return {"Neural": "Nine"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")