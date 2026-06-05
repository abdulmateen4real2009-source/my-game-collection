import socket
import threading

HOST = input("Server IP: ")
PORT = 5555

nickname = input("Nickname: ")

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

def receive():

    while True:

        try:

            message = client.recv(1024).decode()

            print(message)

        except:
            break

def write():

    while True:

        text = input()

        message = f"[{nickname}] {text}"

        client.send(message.encode())

threading.Thread(target=receive, daemon=True).start()

write()
