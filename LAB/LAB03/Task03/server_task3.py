import socket
import threading

data = 8
port = 6666
format = 'utf-8'

device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
server_socket_address = (server_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)
server.listen()

print(f"Server ip :{server_ip}:{port}. Multi-threaded Server is listening..... ")

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    connected = True
    while connected:
        try:
            header = conn.recv(data).decode(format)
            if not header:
                connected = False
                break
            
            upcoming_message_length = int(header)
            message = conn.recv(upcoming_message_length).decode(format)
            
            if message == "Disconnect":
                connected = False
                conn.send("Goodbye".encode(format))
            else:
                num_vowels = count_vowels(message)
                if num_vowels == 0:
                    reply = "Not enough vowels"
                elif num_vowels <= 2:
                    reply = "Enough vowels I guess"
                else:
                    reply = "Too many vowels"
                
                conn.send(reply.encode(format))
        except ValueError:
            connected = False
            
    conn.close()
    print(f"Connection closed: {addr}")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()