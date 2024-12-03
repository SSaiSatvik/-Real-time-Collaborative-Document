@echo off

REM Compile protobuf files
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. doc.proto


if %errorlevel% neq 0 (
    echo Failed to compile protobuf files.
    exit /b %errorlevel%
)


echo Build completed successfully.

REM Start Logger
start cmd /k "python3 logger.py"

REM Start Server
start cmd /k "python3 server.py"

REM Start Client 1
start cmd /k "python3 client.py"

REM Start Client 2
start cmd /k "python3 client.py"

echo All components started successfully.
pause