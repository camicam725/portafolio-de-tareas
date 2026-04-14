import socket
import threading

# configuración
local_host = "127.0.0.1"
local_port = 9000

remote_host = "www.google.com"
remote_port = 80

def handle_client(client_socket):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    # recibir del cliente
    request = client_socket.recv(4096)
    print("[==>] Enviando a remoto...")
    print(request.decode(errors="ignore"))

    remote_socket.send(request)

    # recibir del remoto
    response = remote_socket.recv(4096)
    print("[<==] Respuesta recibida")
    
    client_socket.send(response)

    client_socket.close()
    remote_socket.close()

def server_loop():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, local_port))
    server.listen(5)

    print(f"[*] Escuchando en {local_host}:{local_port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Conexión desde {addr[0]}:{addr[1]}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

server_loop()