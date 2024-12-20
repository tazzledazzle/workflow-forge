from concurrent import futures
import grpc
import task_service_pb2
import task_service_pb2_grpc

class TaskServiceServicer(task_service_pb2_grpc.TaskServiceServicer):
    def NotifyTask(self, request, context):
        print(f"Received task event: {request.event_type} for task ID: {request.task_id}")
        # Process the task event (e.g., forward to Notification Service)
        return task_service_pb2.NotificationAck(message="Task event processed successfully.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_service_pb2_grpc.add_TaskServiceServicer_to_server(TaskServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Task Service gRPC server is running on port 50051.")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
