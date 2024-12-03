import grpc
from concurrent import futures
import doc_pb2
import doc_pb2_grpc
import asyncio


class DocServicer(doc_pb2_grpc.CollaborativeDocumentServicer):
    def __init__(self):
        self.doc = ""
        self.clients = {}

        self.logger_channel = grpc.aio.insecure_channel('localhost:50052')
        self.logger_stub = doc_pb2_grpc.LoggerStub(self.logger_channel)
    
    async def EditDocument(self, request_iterator, context):
        metadata = dict(context.invocation_metadata())
        client_id = metadata.get('client-id')
        self.clients[client_id]=context
        
        try:
            async for edit in request_iterator:
                if edit.is_initial:
                    print(f"Client {client_id} connected.")
                    await context.write(doc_pb2.Transfer(type_operation="insert", position=0, data=self.doc))
                else:
                    self.update_doc(edit)
                    await self.send_to_clients(edit,client_id)

                    log_entry = doc_pb2.LogEntry(client_id=client_id, type_operation=edit.type_operation, data=edit.data, position=edit.position)
                    try:
                        await self.logger_stub.LogChanges(log_entry)
                        print(f"Logged change from client {client_id}.")
                    except grpc.RpcError as e:
                        print(f"Failed to log change: {e}")

        except grpc.RpcError as e:
            print(f"Error with client {client_id}: {e}")
            del self.clients[client_id]

    def update_doc(self, edit):
        if edit.type_operation=="insert":
            self.doc = self.doc[:edit.position] + edit.data + self.doc[edit.position:]
        elif edit.type_operation=="delete":
            self.doc = self.doc[:edit.position] + self.doc[(edit.position+len(edit.data)):]
        
        print(f"Doc updated: {self.doc}")

    async def send_to_clients(self, edit, actual_client_id):
        print(f"Sending update to all clients.")
        for client_id, client_context in list(self.clients.items()):
            if actual_client_id != client_id:
                try:
                    await client_context.write(edit)
                    print(f"Sent update to client {client_id}.")
                except grpc.RpcError as e:
                    print(f"Failed to send update to client {client_id}: {e}")
                    del self.clients[client_id]


async def main():
    server = grpc.aio.server()

    doc_pb2_grpc.add_CollaborativeDocumentServicer_to_server(DocServicer(), server)

    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
