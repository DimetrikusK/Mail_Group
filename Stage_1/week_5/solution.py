import socket
import time


# sock = socket.create_connection(("127.0.0.1", 12223))
# sock.sendall(b"ping")
# sock.close()
# class Error:
#     pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout= timeout
        self.sock = socket.create_connection((self.host, self.port), timeout)


    def put(self, key, value, timestamp=None):
        if not timestamp:
            timestamp = str(int(time.time()))
        send = f'put {key} {value} {timestamp}\n'.encode('utf-8')
        self.sock.sendall(send)
        server = self.sock.recv(1024)
        if b'ok\n' not in server:
            raise Exception

    def get(self):
        pass

