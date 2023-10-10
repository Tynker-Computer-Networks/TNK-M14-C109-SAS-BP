import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

print("Server has started...")

# Create an infinite while loop

    # Call server.accept() method ans receive two values in conn and addr variables
    
    
    # Use conn.send to send encoded message to a new client
    
    # Close the connection
    