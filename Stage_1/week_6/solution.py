import asyncio

storage = dict()


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
    command = data.split()
    if command:
        if command[0] != 'put' and command[0] != 'get':
            return "error\nwrong command\n\n"
        elif command[0] == 'put' and len(command) == 4:
            return sever_put(command[1], command[2], command[3])
        elif command[0] == 'get':
            return sever_get(command)
    else:
        return "error\nwrong command\n\n"


def sever_put(key, value, time):
    try:
        float(value)
        float(time)
        if not key in storage:
            storage[key] = list()
        if not (time, value) in storage[key]:
            storage[key].append((time, value))
            storage[key].sort(key=lambda x: x[0])
        return 'ok\n\n'
    except ValueError:
        return "error\nwrong command\n\n"


def sever_get(command):
    send = 'ok\n'
    string = ''
    try:
        if command and command[1] and len(command) == 2:
            if len(storage) == 0:
                return 'ok\n\n'
            if command[1] == '*':
                for key, values in storage.items():
                    for value in values:
                        string += key + ' ' + value[1] + ' ' + value[0] + '\n'
                return send + string + '\n'
            else:
                if command[1] in storage:
                    for value in storage[command[1]]:
                        string += command[1] + ' ' + value[1] + ' ' + value[0] + '\n'
                return send + string + '\n'
    except:
        return "error\nwrong command\n\n"
    #

# run_server('127.0.0.1', 2225)
