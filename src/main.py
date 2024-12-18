"""
    frontendClient
"""
import asyncio
import requests
import websockets

BASE_URL = "http://127.0.0.1:8000"

# Example interaction
async def main():
    """
    frontend_client
    :return:
    """
    timeout = 15.0
    # Login and get token
    response = requests.post(f"{BASE_URL}/login/", json={"username": "admin", "password": "admin"},
                             timeout=timeout)
    token = response.json().get("access_token")
    headers = {"Authorization": f"Bearer {token}"}

    # Create a task
    task_data = {"name": "Test Task", "description": "This is a test task"}
    requests.post(f"{BASE_URL}/tasks/", json=task_data, headers=headers, timeout=timeout)

    # Listen to WebSocket notifications
    async with websockets.connect("ws://127.0.0.1:8000/ws") as websocket:
        await websocket.send("Task created!")
        while True:
            message = await websocket.recv()
            print(f"Notification: {message}")

asyncio.run(main())
#
# app = FastAPI()
# clients: List[WebSocket] = []
# tasks = TaskService()
#
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     clients.append(websocket)
#     while True:
#         data = await websocket.receive_text()
#         for client in clients:
#             await client.send_text(f"Message: {data}")
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#
# @app.get("/tasks")
# async def list_tasks():
#     found_tasks = tasks.list_tasks()
#     return {"message": "Tasks in List", "tasks": found_tasks }
#
# @app.post("/tasks/")
# def create_task(task: Task):
#     # Logic to save task in DB
#     # id: int
#     # title: str
#     # description: str
#     # status: str
#     tasks.save_task(task.title, task.description, task.status)
#     return {"message": "Task created", "task": task}
