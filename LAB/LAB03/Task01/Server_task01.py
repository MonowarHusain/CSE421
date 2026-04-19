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

print(f"Server ip :{server_ip}:{port}. Server is listening..... ")

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
                
            upcoming_message_length = header
            print("Upcoming message length is:", upcoming_message_length)

            if upcoming_message_length:
               
                message = conn.recv(int(upcoming_message_length)).decode(format)
                print("Server recieved:", message)
                
                if message == "Disconnect":
                    connected = False   
                    print("Client requested disconnect.")

                conn.send("Message recieved".encode(format))
                
        except ValueError:
            connected = False

   
    conn.close()
    print(f"Connection with {addr} closed.")