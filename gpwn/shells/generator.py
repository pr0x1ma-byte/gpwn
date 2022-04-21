from gpwn.shells import C, Php


class ShellGenerator:
    def __init__(self, args):
        self.port = args.shell_port
        self.address = args.shell_address

        self.type = args.shell_type
        self.format = args.shell_format

    def generate(self):
        shell = self.get_shell()
        if self.type == 'bind':
            shell.generate_bind_shell()
        if self.type == 'reverse':
            shell.generate_reverse_shell()

    def get_shell(self):
        shell = C(address=self.address, port=self.port)
        if self.format == 'php':
            shell = Php(address=self.address, port=self.port)

        return shell
