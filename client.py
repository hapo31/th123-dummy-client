import socket
import sys
from time import sleep

from bytestructure import th123_packet


host = sys.argv[1] if len(sys.argv) >= 2 else '127.0.0.1'
port = port = int(sys.argv[2]) if len(sys.argv) >= 3 and int(sys.argv[1]) < 65536 else 10800

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet = th123_packet()

print("send to :%d" % port)

while not packet.end():
    data = packet.next()
    print (data)
    sock.sendto(packet.next(), (host, port))
    sleep(1/60)
    # data, _ = sock.recvfrom(1024)
    # print (data.hex())