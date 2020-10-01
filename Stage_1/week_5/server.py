import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 12223))
sock.listen()

conn, addr = sock.accept()
# print('Соединение установлено:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))

conn.close()
sock.close()

