import socket
import time


class ClientError(Exception):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = (timeout or int(time.time()))
        try:
            self.sock = socket.create_connection((self.host, self.port), self.timeout)
        except socket.error as err:
            raise ClientError(err)

    def put(self, key, value, timestamp=None):
        timestamp = (timestamp or int(time.time()))
        send = f'put {key} {value} {timestamp}\n'.encode('utf-8')
        try:
            self.sock.sendall(send)
            server = self.sock.recv(1024)
            if b'ok' not in server:
                raise ClientError
        except Exception:
            raise ClientError

    def get(self, key):
        dick_metric = {}
        send = f'get {key}\n'.encode('utf-8')
        try:
            self.sock.sendall(send)
            server = self.sock.recv(1024)
            if b'ok\n' not in server:
                raise ClientError

            server = str(server).strip('\n').split('\\n')

            for m in server:
                metrics = m.split(' ')
                if len(metrics) == 3:
                    metric_key = metrics[0]
                    metric_value = float(metrics[1])
                    metric_timestamp = int(metrics[2])
                    metric_list = dick_metric.get(metric_key, [])
                    metric_list.append((metric_timestamp, metric_value))
                    dick_metric.update({metric_key: sorted(metric_list)})
                elif metrics not in [["b'ok"], [""], ["'"]]:
                    raise ClientError
            return dick_metric
        except Exception:
            raise ClientError



# client = Client("127.0.0.1", 2222, timeout=15)
# print(client.get("*"))
# client.put("eardrum.cpu", 4, timestamp=1150864251)
# client.get("eardrum.memory")