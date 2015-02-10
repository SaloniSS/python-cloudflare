import logging

DEBUG = 0
INFO = 1

class Logger:
    def __init__(self, level):
        self.logger_level = self.get_level(level)

    def getLogger(self):
        # create logger
        logger = logging.getLogger('Python CloudFlare API v4')
        logger.setLevel(self.logger_level)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        return logger

    def get_level(self, level):
        if level == 0:
            return logging.DEBUG
        else:
            return logging.INFO
