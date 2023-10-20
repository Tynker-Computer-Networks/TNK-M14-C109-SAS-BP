import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()


print("Server has started...")

while True:
    conn, addr = server.accept()
    
    # Print Client connected
    print("Client connected")

    conn.send("Thank you for connecting".encode())
    conn.close()