# # реализация сервера для тестирования метода get по заданию - Клиент для отправки метрик
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import socket
#
# sock = socket.socket()
# sock.bind(('127.0.0.1', 2223))
# sock.listen(1)
# conn, addr = sock.accept()
# tmp = []
# print('Соединение установлено:', addr)
#
# # response = b''
# response = b'ok\npalm.cpu 10.5 1501864247\n\n'
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
#
# while True:
#     data = conn.recv(1024)
#     if not data:
#         break
#     request = data.decode('utf-8')
#     print(f'Получен запрос: {ascii(request)}')
#     print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
#     conn.send(response)
#
# conn.close()


# string = 'get em.cpu\n'
# i = 'em.cpu 4 1150864251\n'
# # print(string.find('\n'))
# print(string[4:] == i[0:len(string[4:])])
#
# or tmp == "error\nwrong command\n\n" or tmp == "error"



# def run_server(host, port):
#     global stack
#     global new_stack
#     stack = []
#     new_stack = []
#
#     async def metric_server(reader, writer):
#         data = await reader.read(1024)
#         message = data.decode('utf-8')
#         addr = writer.get_extra_info("peername")
#         command = ClientServerProtocol(message)
#         tmp = (command.data_received())
#         if tmp == 'ok':
#             writer.write(b'ok\n\n')
#         elif tmp == "error\nwrong command\n\n":
#             writer.write(b'error\nwrong command\n')
#         else:
#             for i in tmp:
#                 send = 'ok\n' + i[0:] + '\n'
#                 writer.write(send.encode())
#     loop = asyncio.get_event_loop()
#     coro = asyncio.start_server(metric_server, host, port, loop=loop)
#     server = loop.run_until_complete(coro)
#     try:
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#     server.close()
#     loop.run_until_complete(server.wait_closed())
#     loop.close()


# class ClientServerProtocol:
#
#     def __init__(self, command):
#         self.command = command.split()
#         self.string = command
#
#     def data_received(self):
#         if self.command[0] != 'put' and self.command[0] != 'get':
#             return "error\nwrong command\n\n"
#         elif self.command[0] == 'put' and len(self.command) != 4:
#             return "error\nwrong command\n\n"
#         elif self.command[0] == 'get' and len(self.command) > 2:
#             return "error\nwrong command\n\n"
#         elif self.command[0] == 'put':
#             stack.append(self.string[4:])
#             return 'ok'
#         elif self.command[0] == 'get':
#             if self.command[1] == '*':
#                 if len(stack) > 0:
#                     return stack
#                 else:
#                     return "ok"
#             else:
#                 for i in stack:
#                     if self.string[4:self.string.find('\n')] == i[0:len(self.string[4:self.string.find('\n')])]:
#                         new_stack.append(i)
#                 return new_stack




# def proces_received(data):
#     command = data.split(' ')
#     if command[0] == "get":
#         return get(command)
#     elif command[0] == "put":
#         return put(command)
#     return "error\nwrong command\n\n"
#
#
# def put(command):
#     if len(command) == 4:
#         server_response = "ok\n\n"
#         key, value, time = command[1], float(command[2]), int(command[3])
#         if key in storage:
#             old_data = storage[key]
#             for idx, metric_values in enumerate(old_data):
#                 if metric_values[0] == time:
#                     old_data.remove((metric_values[0], metric_values[1]))
#                     break
#             old_data.append((time, value))
#             storage[key].sort(key=lambda x: x[0])
#         else:
#             storage[key] = [(time, value)]
#         # print(storage)
#         return server_response
#     return "error\n\n"
#
#
# def get(command):
#     to_find = command[1][0:-1]
#     if len(command) == 2:
#         server_response = "ok\n"
#         if to_find == "*":
#             for key, value_list in storage.items():
#                 for params in value_list:
#                     server_response += "{} {} {}\n".format(key, params[1], params[0])
#         elif to_find in storage:
#             for value in storage[to_find]:
#                 server_response += "{} {} {}\n".format(to_find, value[1], value[0])
#         server_response += "\n"
#         # print(server_response)
#         return server_response
#     return "error\n\n"
#
#
# run_server('127.0.0.1', 2223)



i = 'em.cpu 4 1150864251\n'
comand = '23'
try:
    float(comand)
except ValueError:
    print('error')
