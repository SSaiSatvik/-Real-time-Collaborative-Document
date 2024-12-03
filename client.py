import grpc
import curses
import time
import uuid
import doc_pb2
import doc_pb2_grpc
from google.protobuf.empty_pb2 import Empty
import asyncio

class Client:
    def __init__(self, channel):
        self.stub = doc_pb2_grpc.CollaborativeDocumentStub(channel)
        self.client_id = str(uuid.uuid4())
        self.metadata = [('client-id', self.client_id)]
        self.data=""
        self.cursor = 0
        self.stream =  None

    async def stream_doc(self):
        try:
            self.stream = self.stub.EditDocument(metadata=self.metadata)
            await self.stream.write(doc_pb2.Transfer(is_initial=True))
            asyncio.create_task(self.recieve_edit())
        except grpc.RpcError as e:
            print(f"Failed to connect to server: {e}")
            await self.handle_grpc_failure()
    
    async def recieve_edit(self):
        try:
            async for edit in self.stream:
                if edit.type_operation=="insert":
                    self.data = self.data[:edit.position] + edit.data + self.data[edit.position:]
                elif edit.type_operation=="delete":
                    self.data = self.data[:edit.position] + self.data[(edit.position+len(edit.data)):]

                if self.cursor > len(self.data):
                    self.cursor = len(self.data) 
                    
        except grpc.RpcError as e:
            print(f"Error receiving edit: {e}")
            await self.handle_grpc_failure()

    async def send_edit(self, type_operation, position, data):
        try:
            await self.stream.write(doc_pb2.Transfer(type_operation=type_operation, position=position, data=data, is_initial=False))
        except grpc.RpcError as e:
            print(f"Error sending edit: {e}")
            await self.handle_grpc_failure()

    async def handle_grpc_failure(self):
        print("Reconnecting in 2 seconds.")
        await asyncio.sleep(2)
        await self.stream_doc()

async def main(stdscr):
    channel = grpc.aio.insecure_channel('localhost:50051')
    client = Client(channel)

    await client.stream_doc()

    curses.curs_set(1)  
    stdscr.nodelay(True)  
    stdscr.keypad(True)  

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, client.data)
        stdscr.move(0, client.cursor)
        stdscr.refresh()

        key = stdscr.getch()
        if key != -1:
            if key == ord('q'):
                break
            elif key in (curses.KEY_BACKSPACE, 127, 8): 
                if client.cursor > 0:
                    await client.send_edit("delete", client.cursor - 1, client.data[client.cursor - 1])
                    client.data = client.data[:client.cursor-1] + client.data[client.cursor:]
                    client.cursor -= 1
            elif key == curses.KEY_LEFT: 
                if client.cursor > 0:
                    client.cursor -= 1
            elif key == curses.KEY_RIGHT:
                if client.cursor < len(client.data):
                    client.cursor += 1
            elif chr(key).isalnum():
                await client.send_edit("insert", client.cursor, chr(key))
                client.data = client.data[:client.cursor] + chr(key) + client.data[client.cursor:]
                client.cursor += 1

        await asyncio.sleep(0.01)


if __name__ == "__main__":
    curses.wrapper(lambda stdscr: asyncio.run(main(stdscr)))


