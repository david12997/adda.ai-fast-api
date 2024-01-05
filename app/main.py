from typing import Union
from fastapi import FastAPI
from .routes.router import addaRouter



app = FastAPI()
app.title = "Adda API"
app.version = "0.0.1"

app.include_router(addaRouter)