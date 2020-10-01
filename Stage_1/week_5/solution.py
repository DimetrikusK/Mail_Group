import socket
import time


class ClientError(Exception):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = (timeout or time.time())
        try:
            self.sock = socket.create_connection((self.host, self.port), self.timeout)
            server = self.sock.recv(1024)
            if b'ok\n' not in server:
                ClientError(Exception)
        except:
            ClientError(Exception)

    def put(self, key, value, timestamp=None):
        timestamp = (timestamp or time.time())
        send = f'put {key} {value} {timestamp}\n'.encode('utf-8')
        self.sock.sendall(send)

    def get(self, key):
        dick_metric = {}
