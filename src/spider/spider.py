'''
Created on 2018年4月6日

@author: Loong
'''
from util.logutil import logger
from config import configs
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Spider():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    urls = set()   

    def get_projectname(self):
        return configs['projectname']
    
    def get_developers(self):
        return configs['developer']

    def create_custname_url(self, custname):
        return custname
    
    def create_developer_url(self, developer):
        return developer

    def get_statistics_cust(self, url):
        return {'custname':url, 'num1':'1', 'num2':'2', 'num3':'3', 'num4':'4'}
    
    def do_statistics_cust(self):
        statistics_cust = list()
        # 1、根据客户列表进行jira统计
        projectnames = self.get_projectname()
        for custname in projectnames:
            custstatistics = self.get_statistics_cust(custname)
            statistics_cust.append(custstatistics)
        return statistics_cust

    def get_statistics_dev(self, url):
        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser");
        return {'devname':url, 'num1':'1', 'num2':'2', 'num3':'3', 'num4':'4'}
    
    def do_statistics_dev(self):
        statistics_dev = list()
        # 2、根据开发者列表进行jira统计
        developers = self.get_developers()
        for developer in developers:
            devstatistics = self.get_statistics_dev(developer)
            statistics_dev.append(devstatistics)
        return statistics_dev    

    def create_report_html(self, statistics_cust, statistics_dev):
        # 3、生成report
        if statistics_cust is None and statistics_dev is None:
            return None
        
        report = "<body>"
        report += "<table border='1' cellspacing='0'>"   
        report += "<tr style='background-Color:#DDDDDD'>" 
        report += "<th>" + "客户名称" + "</th>" 
        report += "<th>" + "上期剩余" + "</th>" 
        report += "<th>" + "本期新增" + "</th>" 
        report += "<th>" + "本期解决" + "</th>" 
        report += "<th>" + "待处理总计" + "</th>" 
        report += "</tr>" 
        for cust in statistics_cust:
            report += "<tr>" 
            report += "<td>" + cust['custname'] + "</td>" 
            report += "<td>" + cust['num1'] + "</td>" 
            report += "<td>" + cust['num2'] + "</td>" 
            report += "<td>" + cust['num3'] + "</td>" 
            report += "<td>" + cust['num4'] + "</td>" 
            report += "</tr>" 
        report += "</table>"  
        
        report += "<br/>"  
        report += "<br/>"  
          
        report += "<table border='1' cellspacing='0'>"
        report += "<tr style='background-Color:#DDDDDD'>" 
        report += "<th>" + "开发者" + "</th>" 
        report += "<th>" + "上期剩余" + "</th>" 
        report += "<th>" + "本期新增" + "</th>" 
        report += "<th>" + "本期解决" + "</th>" 
        report += "<th>" + "待处理总计" + "</th>" 
        report += "</tr>"         
        for dev in statistics_dev:
            report += "<tr>" 
            report += "<td>" + dev['devname'] + "</td>" 
            report += "<td>" + dev['num1'] + "</td>" 
            report += "<td>" + dev['num2'] + "</td>" 
            report += "<td>" + dev['num3'] + "</td>" 
            report += "<td>" + dev['num4'] + "</td>" 
            report += "</tr>"             
        report += "</table>"    
        report += "</body>"
        return report
    
    def createReport(self):
        statistics_cust = self.do_statistics_cust()
        statistics_dev = self.do_statistics_dev()
        report_html = self.create_report_html(statistics_cust, statistics_dev)
        return report_html

    
if __name__ == '__main__':
    logger.info(Spider().createReport());    
