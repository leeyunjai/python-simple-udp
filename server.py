import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 1234))

while True:
  data, addr = sock.recvfrom(200)
  print("Received data:", data.decode())
  print("Client:", addr[0], addr[1])
