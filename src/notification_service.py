"""
    Notification Service
"""
import typing
from fastapi import FastAPI, WebSocket

app = FastAPI()
connected_clients: typing.List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    real-time tasks
    :param websocket:
    :return:
    """
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                await client.send_text(data)
    except RuntimeError as e:
        connected_clients.remove(websocket)
        print(f"{e}")
    finally:
        pass
