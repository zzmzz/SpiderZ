import logging
from Utils.config import Config


class LogFactory:
    logging.basicConfig()

    @staticmethod
    def getlogger(name):
        logger = logging.getLogger(name)
        logger.setLevel(LogFactory.__get_logger_level(Config.getProperty("logger", "level")))
        return logger

    @staticmethod
    def __get_logger_level(level):
        if level == "DEBUG":
            return logging.DEBUG
        elif level == "INFO":
            return logging.INFO
        elif level == "ERROR":
            return logging.ERROR
        else:
            return logging.NOTSET
