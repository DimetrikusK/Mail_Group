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


client = Client("127.0.0.1", 2227, timeout=15)
client.put("test_float_value", 42, timestamp=503319345)
client.put("test_multivalue_key", 10.678, timestamp=1503319748)
client.put("test_multivalue_key", 12.5, timestamp=1503319748)
# client.put("tes2t_key", 12.0, timestamp=1503319742)
# client.put("palm.cpu", 23.7, timestamp=1503319740)
# client.put("*")client_input0
# print(client.get("test_multivalue_key"))
print(client.get("*"))
# client.put("em.cpu", 4, timestamp=1150864251)

# test_multivalue_key 12.0 1503319740
# test_multivalue_key 10.678 1503319748
#

# import socket
# conn = socket.create_connection(('127.0.0.1', 2224))
# command = f'get {"*"}\n'
# conn.sendall(command.encode())
# data = conn.recv(2048).decode('utf-8')
# conn.close()
# print(ascii(data))


# # command = f'put {"ntest_key"} {12.0} {1503319740}\n'