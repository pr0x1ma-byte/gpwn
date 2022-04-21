from gpwn.log import configure_logging
from gpwn.shells.generator import ShellGenerator
import logging
import argparse

parser = argparse.ArgumentParser(description='Pwn that machine!')
parser.add_argument('--debug', dest='debug', default=False, action='store_true', help="enable debug logging")

subparser = parser.add_subparsers(dest='shell', help='shell sub-command help')
shell_parser = subparser.add_parser('shell', help='shell help')
shell_parser.add_argument('-t', dest='shell_type', choices=['bind', 'reverse'], help='specify shell behavior',
                          required=True)
shell_parser.add_argument('-f', dest='shell_format', choices=['binary', 'php'], help='specify shell output format',
                          required=True)

shell_parser.add_argument('-a', dest='shell_address', type=str, default='127.0.0.1', help="remote address or host")
shell_parser.add_argument('-p', dest='shell_port', type=int, default='8080', help="remote port")

args = parser.parse_args()
if args.debug:
    level = 'DEBUG'
configure_logging(level)

logger = logging.getLogger().getChild(__name__)

if __name__ == '__main__':

    if args.shell is not None:
        logger.debug("creating a %s %s shell", args.shell_format, args.shell_type)
        ShellGenerator(args).generate()
