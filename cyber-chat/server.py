import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print(f"Cyber Chat Server Running on Port {PORT}")

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def handle(client):

    while True:

        try:
            message = client.recv(1024)

            if not message:
                break

            broadcast(message)

        except:
            break

    clients.remove(client)
    client.close()

while True:

    client, address = server.accept()

    print(f"Connected: {address}")

    clients.append(client)

    thread = threading.Thread(
        target=handle,
        args=(client,)
    )

    thread.start()
