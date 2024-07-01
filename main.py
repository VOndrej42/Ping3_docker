from ping3 import ping
import time

server = '8.8.8.8'

while True:
    print(ping(server))
    time.sleep((2))
