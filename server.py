import orjson
import asyncio
import platform
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


def dumps(data):
    """Helper to dump JSON using orjson, returning a UTF-8 string."""
    return orjson.dumps(data).decode('utf-8')


class ConnectionManager:
    def __init__(self):
        self.active_connections = set()
        self.clients_data = {}
        self.ws_to_client = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.discard(websocket)
        client_id = self.ws_to_client.pop(websocket, None)
        if client_id:
            self.clients_data.pop(client_id, None)

    async def broadcast(self, message: str):
        if self.active_connections:
            await asyncio.gather(
                *[ws.send_text(message) for ws in self.active_connections],
                return_exceptions=True
            )

    async def update_client(self, client_id: str, data: dict, websocket: WebSocket):
        self.ws_to_client[websocket] = client_id
        if client_id in self.clients_data:
            self.clients_data[client_id].update(data)
        else:
            self.clients_data[client_id] = data

        payload = {"type": "update", "clients": [
            {**d, "ws": None} for d in self.clients_data.values()]}
        await self.broadcast(dumps(payload))


manager = ConnectionManager()


@app.get("/")
async def get():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            try:
                json_data = orjson.loads(data)
            except orjson.JSONDecodeError:
                continue

            client_id = json_data.get("id")
            if client_id:
                await manager.update_client(client_id, json_data, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        payload = {"type": "update", "clients": [
            {**d, "ws": None} for d in manager.clients_data.values()]}
        await manager.broadcast(dumps(payload))


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
