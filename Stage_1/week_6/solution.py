import asyncio

storage = {}
stack = []
new_stack = []
send = 'ok\n'


class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = proces_received(data.decode())
        if resp is None:
            resp = "error\nwrong command\n\n"
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


def proces_received(data):
    string = data
    command = data.split()
    if command:
        if command[0] != 'put' and command[0] != 'get':
            return "error\nwrong command\n\n"
        elif command[0] == 'put':
            return sever_put(command, string)
        elif command[0] == 'get':
            return sever_get(command, string)
    else:
        return "error\nwrong command\n\n"


def sever_put(command, string):
    global stack
    try:
        if len(command) == 4:
            float(command[2])
            float(command[3])
            stack.append(string[4:])
            return 'ok\n\n'
    except ValueError:
        return "error\nwrong command\n\n"


def sever_get(command, string):
    global send
    try:
        if command and command[1] and len(command) == 2:
            if len(stack) == 0:
                return 'ok\n\n'
            if command[1] == '*':
                for i in stack:
                    send += i[0:]
                return send + '\n'
            if str(command[1]):
                for i in stack:
                    if string[4:string.find('\n')] == i[0:len(string[4:string.find('\n')])]:
                        send += i
                return send + '\n'
    except:
        return "error\nwrong command\n\n"

# run_server('127.0.0.1', 2224)
