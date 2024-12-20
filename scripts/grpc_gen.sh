#!/usr/bin/env bash


## Use `grpcio-tools` to generate Python code from the .proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. task_service.proto
