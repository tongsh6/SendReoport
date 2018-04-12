# -*- coding: utf-8 -*-
'''
Created on 2018年4月6日

@author: Loong
'''
import smtplib
from util.logutil import logger
from config import configs
from email.mime.text import MIMEText
from email.header import Header
# -*- coding: utf-8 -*-


class MailSender():
    '''
    发送邮件
    '''
    
    def __init__(self):
        '''
        邮件工具构造器
        '''

    def get_sender_info(self):
        return configs['sendmailinfo']['user'], configs['sendmailinfo']['password']
    
    def get_recinfos(self):
        return configs['recmailinfo']
    
    def get_smtp_server(self):
        return configs['sendmailinfo']['smtp'], configs['sendmailinfo']['port']

    def get_ccinfos(self):
        return configs['ccmailinfo']

    def get_subject(self):
        return configs['subject']
    
    def sendReport(self, report=None):
        if report is None:
            logger.info("report is None")
            return 
        
        # 获取发件人信息 地址和密码
        from_addr, password = self.get_sender_info()
        logger.debug("from_addr:" + from_addr + ",password:" + password)
        # 获取发件邮箱服务器
        smtp_server, port = self.get_smtp_server()
        logger.debug("smtp_server:" + smtp_server)
        # 获取收件人信息
        to_addr = self.get_recinfos()
        for toaddr in to_addr:
            logger.debug("to_addr:" + toaddr)
        # 获取抄送人信息
        cc_addr = self.get_ccinfos()
        for cc in cc_addr:
            logger.debug("cc_addr:" + cc)
        subject = self.get_subject()    
        # 发送邮件
        msg = MIMEText(report, 'html', 'utf-8')
        msg['From'] = from_addr
        msg['To'] = ','.join(to_addr)
        msg['CC'] = ', '.join(cc_addr)  
        msg['Subject'] = Header(subject, 'utf-8').encode()
        server = smtplib.SMTP(smtp_server, port)
        server.set_debuglevel(1)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        return;

        
if __name__ == '__main__':
    MailSender().sendReport("九恒星")
