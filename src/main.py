# -*- coding: utf-8 -*-
'''
Created on 2018年4月6日

@author: Loong
'''
from spider.spider import Spider
from mail.mailsender import MailSender
from util.logutil import logger


class ReportMain():

    def __init__(self):
        self.spider = Spider()
        self.mailsender = MailSender()
            
    def startup(self):
        logger.info("start up .")

        report = self.spider.createReport()
        
        self.mailsender.sendReport(report)
        
        logger.info("end .")


if __name__ == '__main__':
    ReportMain().startup()
