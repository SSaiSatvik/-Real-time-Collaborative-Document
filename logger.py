import doc_pb2
import doc_pb2_grpc
import asyncio
import grpc
from google.protobuf.empty_pb2 import Empty

class LoggerServicer(doc_pb2_grpc.LoggerServicer):
    def __init__(self, log_file="document_changes.log"):
        self.log_file = log_file

    async def LogChanges(self, request, context):
        with open(self.log_file, "a") as f:
            log_entry = f"Client ID: {request.client_id}, Operation: {request.type_operation}, Position: {request.position}, Data: {request.data}\n"
            f.write(log_entry)
            print(f"Logged: {log_entry.strip()}")
        return Empty()
    
async def main():
    logger = grpc.aio.server()
    doc_pb2_grpc.add_LoggerServicer_to_server(LoggerServicer(), logger)
    print("Logger server starting on port 50052...")
    logger.add_insecure_port('[::]:50052')
    await logger.start()
    await logger.wait_for_termination()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Logger server stopped.")

