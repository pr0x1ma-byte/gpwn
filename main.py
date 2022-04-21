from gpwn.log import configure_logging

configure_logging()

import logging
import argparse

logger = logging.getLogger().getChild(__name__)


parser = argparse.ArgumentParser(description='Pwn that machine!')
parser.add_argument('--debug', dest='debug', default=False, action='store_true', help="enable debug logging")
#parser.add_argument(['--payload', '-p'], choices=['c', 'php'], default=None, help="specify shell format")
#parser.add_argument(['--type', '-t'], choices=['bind', 'reverse'], default = None, help="specify shell type")
parser.add_argument('-ra', dest='raddress', default=None, help="remote address")
parser.add_argument('-rp', dest='rport', default = None, help="remote port")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.debug:
        logger.setLevel('DEBUG')

    logger.debug("args: %s", args)


        
