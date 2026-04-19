import socket

data = 8
port = 6666
format = 'utf-8'

device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
server_socket_address = (server_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)
server.listen()

print(f"Server ip :{server_ip}:{port}. Salary Server is listening..... ")

def calculate_salary(hours):
    if hours <= 40:
        return hours * 200
    else:
        return 8000 + ((hours - 40) * 300)

while True:
    conn, addr = server.accept()
    print(f"Connected to {addr}")
    
    connected = True
    while connected:
        try:
            header = conn.recv(data).decode(format)
            if not header:
                connected = False
                break
            
            upcoming_message_length = int(header)
            message = conn.recv(upcoming_message_length).decode(format)
            print("Server recieved hours:", message)
            
            if message == "Disconnect":
                connected = False
                conn.send("Goodbye".encode(format))
            else:
                try:
                    hours = int(message)
                    salary = calculate_salary(hours)
                    reply = f"Salary: Tk {salary}"
                except ValueError:
                    reply = "Invalid input. Please send a number."
                
                conn.send(reply.encode(format))
                
        except ValueError:
            connected = False

    conn.close()