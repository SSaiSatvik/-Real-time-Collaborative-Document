# Collaborative Document System

This project implements a collaborative document editing system using gRPC. It includes a server, a logger, and clients that can edit the document collaboratively.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `grpcio` and `grpcio-tools` packages
- `protobuf` package

## Installation

1. **Clone the repository**:
    ```sh
    cd <repository_directory>
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install grpcio grpcio-tools protobuf
    ```

5. **Compile the protobuf files**:
    ```sh
    python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. doc.proto
    ```

## Running the System

1. **Start the Logger**:
    ```sh
    python3 logger.py
    ```

2. **Start the Server**:
    ```sh
    python3 server.py
    ```

3. **Start the Clients**:
    ```sh
    python3 client.py
    ```

    Open multiple terminals and run the above command to start multiple clients.

**Alternatively can use run in Windows**:
```sh
run.bat
```

## Protobuf Definitions

The [doc.proto](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5CNothing%5C%5CDocuments%5C%5CSEMISTER%207%5C%5CDISTRIBUTED%20SYSTEMS%5C%5CHW4%5C%5C4%5C%5Cdoc.proto%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FNothing%2FDocuments%2FSEMISTER%207%2FDISTRIBUTED%20SYSTEMS%2FHW4%2F4%2Fdoc.proto%22%2C%22scheme%22%3A%22file%22%7D%7D) file defines the protocol buffer messages and services used in the system.

### Messages

- **Transfer**: Represents a document transfer operation.
    - `string type_operation`: The type of operation (e.g., insert, delete).
    - `string data`: The data being transferred.
    - `int32 position`: The position in the document.
    - `bool is_initial`: Indicates if this is the initial transfer.

- **LogEntry**: Represents a log entry for document changes.
    - `string client_id`: The ID of the client making the change.
    - `string type_operation`: The type of operation.
    - `string data`: The data being logged.
    - `int32 position`: The position in the document.

### Services

- **CollaborativeDocument**: Service for editing the document.
    - `rpc EditDocument(stream Transfer) returns (stream Transfer)`: RPC for editing the document.

- **Logger**: Service for logging document changes.
    - `rpc LogChanges(LogEntry) returns (google.protobuf.Empty)`: RPC for logging changes.
