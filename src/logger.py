import logging
import sys
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter_stdout = logging.Formatter(
    "%(asctime)s | [%(filename)s:%(lineno)d] | %(levelname)s | %(message)s", "%d-%m-%Y %H:%M:%S"
)
formatter_file = logging.Formatter(
    "%(asctime)s | [%(pathname)s:%(lineno)d] | %(levelname)s | %(message)s", "%d-%m-%Y %H:%M:%S"
)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(level=logging.DEBUG)
stdout_handler.setFormatter(fmt=formatter_stdout)

file_handler = RotatingFileHandler(
    filename="logs.log",
    mode="a",
    maxBytes=1e6,
    backupCount=0,
    encoding="UTF-8",
)
file_handler.setLevel(level=logging.DEBUG)
file_handler.setFormatter(fmt=formatter_file)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
