import logging
from logging.handlers import TimedRotatingFileHandler

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logname = "logs/my_app.log"


def get_logger(logger_name):

    if logging.getLogger(logger_name).hasHandlers():
        return logging.getLogger(logger_name)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    logger = time_handler(logger)
    logger.propagate = False
    return logger


def time_handler(logger):

    handler = TimedRotatingFileHandler(filename=logname, when="midnight", interval=1, backupCount=30)
    handler.suffix = "%Y-%m-%d"
    formatter = logging.Formatter(LOG_FORMAT)

    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
