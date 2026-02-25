import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from asyncua import Client
import uvicorn
import json

app = FastAPI()
URL = "opc.tcp://127.0.0.1:4848/freeopcua/server/"

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    async with Client(url=URL) as client:
        idx = await client.get_namespace_index("http://antigravity.ia/opcua")
        obj = client.nodes.objects
        horno = await obj.get_child(f"{idx}:HornoIndustrial")
        t_n = await horno.get_child([f"{idx}:Variables", f"{idx}:Temperatura"])
        c_n = await horno.get_child([f"{idx}:Variables", f"{idx}:ContadorCiclos"])
        
        while True:
            t = await t_n.get_value()
            c = await c_n.get_value()
            await websocket.send_text(json.dumps({"temp": round(t, 2), "ciclos": c}))
            await asyncio.sleep(1)

@app.post("/reset")
async def reset():
    async with Client(url=URL) as client:
        idx = await client.get_namespace_index("http://antigravity.ia/opcua")
        horno = await client.nodes.root.get_child(["0:Objects", f"{idx}:HornoIndustrial"])
        met = await horno.get_child([f"{idx}:Operaciones", f"{idx}:ResetContador"])
        await horno.call_method(met)

@app.get("/")
async def get():
    return HTMLResponse(content=open("d:/Informática/Sistema OPC-UA/index.html", encoding="utf-8").read())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
