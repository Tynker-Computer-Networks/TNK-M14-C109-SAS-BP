import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

# Create a clients empty list

print("Server has started...")

while True:
    conn, addr = server.accept()
    # Get the count of clients in clientCount variable
    
    # Print count of clients when a new client connects to a server
    
    # Append conn to clients
    

    conn.send("Thank you for connecting".encode())
    conn.close()