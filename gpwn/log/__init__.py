import sys
import logging


def configure_logging(level='DEBUG'):
    logger = logging.getLogger()
    stream = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    stream.setFormatter(formatter)
    logger.addHandler(stream)
    logger.setLevel(level)

    #printer = logging.getLogger('printer')
    #stream = logging.StreamHandler(sys.stdout)
    ##formatter = logging.Formatter('%(message)s')
    #stream.setFormatter(formatter)
    #printer.addHandler(stream)
    #printer.setLevel(level)
