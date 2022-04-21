from gpwn.shells import Shell

class Php(Shell):
    def __init__(self, address: str, port: int):
        Shell.__init__(self, address=address, port=port)
