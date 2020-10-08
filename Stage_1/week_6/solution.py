import asyncio


def run_server(host, port):
    global stack
    stack = str

    async def metric_server(reader, writer):
        global stack
        data = await reader.read(1024)
        message = data.decode('utf-8')
        # addr = writer.get_extra_info("peername")
        command = ClientServerProtocol(message)
        stack = (command.data_received())
        print(stack)
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(metric_server, host, port, loop=loop)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol:

    def __init__(self, command):
        self.stack = []
        self.command = command.split()
        self.string = str

    def data_received(self):
        # return self.command[1:]
        if self.command[0] != 'put' and self.command[0] != 'get':
            return "error\nwrong command\n"
        elif self.command[0] == 'put' and len(self.command) != 4:
            return "error\nwrong command\n"
        elif self.command[0] == 'get' and len(self.command) > 2:
            return "error\nwrong command\n"
        elif self.command[0] == 'put':
            for i in range(len(self.command[2:])):
                self.string += ' ' + self.command[i]
            return self.string
        elif self.command[0] == 'get':
            if self.command[1] == '*':
                return self.stack


run_server('127.0.0.1', 2210)
