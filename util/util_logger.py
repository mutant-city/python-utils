""" A utility module for working with loggers """
import logging


def logging_config(level=logging.INFO, log_format='%(asctime)s %(message)s'):
    """ Setup/configure logger for aws cloudwatch formatting."""
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
    logging.basicConfig(level=level, format=log_format)
    return root


def basic_logging_config(level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)
    # logger is an app-wide singleton
    if len(logger.handlers) < 1:
        consoleHandler = logging.StreamHandler()
        logger.addHandler(consoleHandler)
    return logger
