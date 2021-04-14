# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_view():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello_name_view(name: str):
    return f"Hello {name}"

