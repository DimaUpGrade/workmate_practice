class Data:
    """
    Data structure class for packet that can be transfered 
    """
    def __init__(self, data: str, ip: str) -> None:
        self.data = data
        self.ip = ip


class Server:
    """
    Class for imitation server
    """
    def __init__(self) -> None:
        """
        Initialize Server object, create ip and
        buffer for receiving packages
        """
        self.buffer = list()
        self.ip = id(self)
        self.router = None

    def send_data(self, data: Data) -> None:
        """
        Send data to Router object
        """
        if self.router:
            self.router.buffer.append(data)

    def get_data(self) -> list:
        """
        Return all data packages from buffer
        and clear buffer
        """
        messages = self.buffer.copy()
        self.buffer.clear()
        return messages

    def get_ip(self) -> int:
        """
        Return server ip
        """
        return self.ip
        

class Router:
    """
    Class for imitation router
    """
    def __init__(self) -> None:
        """
        Initialize Router object, create buffer for receiving packages
        and dict of linked servers
        """
        self.buffer = list()
        self.servers = dict()

    def link(self, server: Server) -> None:
        """
        Link Server object with current instance of Router
        """
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server: Server) -> None:
        """
        Unlink Server object with current instance of Router
        """
        del self.servers[server.get_ip()]

    def send_data(self) -> None:
        """
        Send all packages to linked Servers
        and clear buffer of receiving packages
        """
        while self.buffer:
            data = self.buffer.pop()
            if data.ip in self.servers.keys():
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
