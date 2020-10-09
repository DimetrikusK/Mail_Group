# реализация сервера для тестирования метода get по заданию - Клиент для отправки метрик
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 2223))
sock.listen(1)
conn, addr = sock.accept()
tmp = []
print('Соединение установлено:', addr)

# response = b''
response = b'ok\npalm.cpu 10.5 1501864247\n\n'
# response = b'ok\npalm.cpu 0.5 1150864247\neardrum.cpu 15.3 1501864259\n\n'
# metric='palm.cpu', value=0.5, timestamp=1150864247
# while True:
#     data = conn.recv(1024)
#     if not data:
#         break
#     request = data.decode('utf-8')
#     tmp.append('ok\n' + request + '\n')
#     print(f'Получен запрос: {ascii(request)}')
#     print(f'Отправлен ответ {ascii(tmp)}')
#     conn.send(b'tmp')
# [["b'ok'"], [""], [""]]
# sock.close()
# conn.close()

while True:
    data = conn.recv(1024)
    if not data:
        break
    request = data.decode('utf-8')
    print(f'Получен запрос: {ascii(request)}')
    print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
    conn.send(response)

conn.close()


# string = 'get em.cpu\n'
# i = 'em.cpu 4 1150864251\n'
# # print(string.find('\n'))
# print(string[4:] == i[0:len(string[4:])])
#
# or tmp == "error\nwrong command\n" or tmp == "error"