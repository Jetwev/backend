import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

    if data.decode("utf-8") == "OK":
        print(f"Recieved right data! -- {data.decode('utf-8')}")
    else:
        print(f"Recieved wrong data! -- {data.decode('utf-8')}")