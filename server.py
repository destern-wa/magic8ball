import socket
from response import Response

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# Reserve a port on the computer
port = 8888

# Bind to the port
s.bind(('', port))
print(f"Socket bound to port {port}")

# Start listening
s.listen(5)
print("Socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    connection, address = s.accept()
    print('\nGot connection from', address)

    # Get data from client
    data_from_client = ''
    while True:
        data = connection.recv(4096)

        # end of data
        if not data:
            break

        data_from_client += data.decode()

        print("Data from client:", data_from_client)
        response = Response.get(data_from_client)
        print("Sending message back: "+ response)
        connection.send(response.encode())

    connection.close()
    print('client disconnected')
