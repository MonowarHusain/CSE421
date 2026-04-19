import socket

data = 8
port = 6666
format = 'utf-8'

device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
server_socket_address = (server_ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)

def sending_message(msg):
    message = msg.encode(format)
    msg_length = len(message)
    msg_length_str = str(msg_length).encode(format)
    msg_length_str += b' ' * (data - len(msg_length_str))

    client.send(msg_length_str)
    client.send(message)    

    sent_from_server = client.recv(128).decode(format)
    print("Sent from server:", sent_from_server)

hours_input = input("Enter hours worked: ")
sending_message(hours_input)

sending_message("Disconnect")
client.close()