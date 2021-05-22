# coding=utf-8
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

LOGFILE = str(os.path.dirname(os.path.abspath(__file__))) + "/wnapi.log"
logger = logging.getLogger('')


def log(loglevel: int, message: str):
    logger.setLevel(loglevel)
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    fh = RotatingFileHandler(LOGFILE, maxBytes=(1048576 * 5), backupCount=3)
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.log(loglevel, message)
    logger.setLevel(logging.ERROR)
