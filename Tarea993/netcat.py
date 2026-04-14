import socket
import threading

target = "127.0.0.1"
port = 9999

def client_sender():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, port))

    while True:
        msg = input(">> ")
        client.send(msg.encode())

        response = client.recv(4096)
        print(response.decode())

def server_loop():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    print(f"[*] Listening on {target}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Connection from {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        if not request:
            break

        print(f"[*] Received: {request.decode()}")
        client_socket.send(b"OK")

# CAMBIA AQUÍ 👇
modo = input("Modo (server/client): ")

if modo == "server":
    server_loop()
else:
    client_sender()