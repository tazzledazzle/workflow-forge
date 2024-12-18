#!/usr/bin/env bash

pip install fastapi uvicorn sqlite3 pydantic jose websockets

##
uvicorn task_service:app --reload --port 8001
uvicorn notification_service:app --reload --port 8002
uvicorn user_service:app --reload --port 8003

###
python frontend_client.py
