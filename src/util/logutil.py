'''
Created on 2018年4月8日

@author: Loong
'''
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(name)-12s [%(filename)s,%(funcName)s,%(lineno)d]: %(message)s')
# create a filehandler
# handler = logging.FileHandler('\logs\send_report.log')
# handler.setLevel(logging.INFO)
# create alogging format
# handler.setFormatter(formatter)
# add thehandlers to the logger

#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler('E:\logs\send_report.log', maxBytes=10*1024*1024,backupCount=15)
Rthandler.setFormatter(formatter)

logger.addHandler(Rthandler)
