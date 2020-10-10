import asyncio


class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = data_received(data.decode())
        self.transport.write(resp.encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


def data_received(data):
    send = 'ok\n'
    stack = []
    new_stack = []
    string = data
    command = data.split()
    if command[0] != 'put' and command[0] != 'get':
        return "error\nwrong command\n"
    elif command[0] == 'put' and len(command) != 4:
        return "error\nwrong command\n"
    elif command[0] == 'get' and len(command) > 2:
        return "error\nwrong command\n"
    elif command[0] == 'put':
        stack.append(string[4:])
        return 'ok\n\n'
    elif command[0] == 'get':
        if command[1] == '*':
            if len(stack) > 0:
                for i in stack:
                    send += i[0:]
                return send + '\n'
            else:
                return "ok\n\n"
        else:
            for i in stack:
                if string[4:string.find('\n')] == i[0:len(string[4:string.find('\n')])]:
                    new_stack.append(i)
            return new_stack

    #     if tmp == 'ok':
    #         writer.write(b'ok\n\n')
    #     elif tmp == "error\nwrong command\n":
    #         writer.write(b'error\nwrong command\n')
    #     else:
    #         for i in tmp:
    #             send = 'ok\n' + i[0:] + '\n'
    #             writer.write(send.encode())
    # loop = asyncio.get_event_loop()


run_server('127.0.0.1', 2223)


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
#         elif tmp == "error\nwrong command\n":
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
#             return "error\nwrong command\n"
#         elif self.command[0] == 'put' and len(self.command) != 4:
#             return "error\nwrong command\n"
#         elif self.command[0] == 'get' and len(self.command) > 2:
#             return "error\nwrong command\n"
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