class Data:
    def __init__(self, data: str, ip: str) -> None:
        self.data = data
        self.ip = ip


class Server:
    def __init__(self) -> None:
        self.buffer = list()
        self.ip = id(self)
        self.router = None

    def send_data(self, data: Data) -> None:
        if self.router:
            self.router.buffer.append(data)

    def get_data(self) -> list:
        messages = self.buffer.copy()
        self.buffer.clear()
        return messages

    def get_ip(self) -> int:
        return self.ip
        

class Router:
    def __init__(self) -> None:
        self.buffer = list()
        self.servers = dict()

    def link(self, server: Server) -> None:
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server: Server) -> None:
        del self.servers[server.get_ip()]

    def send_data(self) -> None:
        while self.buffer:
            data = self.buffer.pop()
            server = self.servers[data.ip]
            server.buffer.append(data.data)


# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()


# print(msg_lst_from)
# print(msg_lst_to)