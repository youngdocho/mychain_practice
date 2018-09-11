import logging.handlers  # logger 인스턴스를 생성 및 로그 레벨 설정

import os

logger = logging.getLogger("crumbs")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

fileHandler = logging.FileHandler(os.getcwd() + '/my.log')
streamHandler = logging.StreamHandler()

fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)


def write(msg, type=None):
    if type == logging.INFO:
        logger.info(msg)
    elif type == logging.DEBUG:
        logger.debug(msg)
    elif type == logging.ERROR:
        logger.error(msg)
    elif type == logging.CRITICAL:
        logger.critical(msg)
    else:
        logger.info(msg)
