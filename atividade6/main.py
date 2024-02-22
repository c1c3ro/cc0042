from typing import Union
import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/data")
def send_data():
    hora = datetime.datetime.now()
    hora = hora.strftime("%d/%m/%Y %H:%M")
    return {"Data e hora": hora}

@app.get("/soma")
def soma_items(a: Union[str, None] = None, b: Union[str, None] = None):
    return {"A soma é": int(a) + int(b)}

@app.get("/multiplicar")
def soma_items(a: Union[str, None] = None, b: Union[str, None] = None):
    return {"A multiplação é": int(a) * int(b)}

@app.get("/dividir")
def soma_items(a: Union[str, None] = None, b: Union[str, None] = None):
    return {"A divisão é": int(a) / int(b)}

@app.get("/subtrair")
def soma_items(a: Union[str, None] = None, b: Union[str, None] = None):
    return {"A subtração é": int(a) - int(b)}

