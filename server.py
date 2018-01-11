import socket
import sys

from bytestructure import th123_packet




host = "127.0.0.1"
port = int(sys.argv[1]) if len(sys.argv) >= 2 and int(sys.argv[1]) < 65536 else 10800
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((host, port))

# while True:
data, addr = sock.recvfrom(1024)
print (data.hex())
res = 3
sock.sendto(res.to_bytes(1, byteorder="little"), addr)