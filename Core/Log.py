import logging


class Log:
    logger = None

    def __init__(self):
        logging.basicConfig(filename="std.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
