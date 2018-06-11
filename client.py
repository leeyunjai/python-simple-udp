import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
  data = input()
  sock.sendto(data.encode(),('themaker.iptime.org',1234))
