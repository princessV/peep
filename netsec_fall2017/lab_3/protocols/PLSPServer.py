from .PLSP import PLSP


class PLSPServer(PLSP):

    def __init__(self):
        super(PLSPServer, self).__init__()

    def connection_made(self, transport):
        self.transport = transport

