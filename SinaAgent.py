#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class SinaAgent(object):

    def __init__(self):
        #成都
#         self.url = 'http://cd.esf.sina.com.cn/agent'
        #重庆
        self.url = 'http://cq.esf.sina.com.cn/agent/'
        self.nodeUrl = 'http://172.28.1.90:5555/wd/hub'
        self.nameList = []        
        self.phoneList = []
        # 创建webdriver远程连接
        try:
            self.driver = webdriver.Remote(command_executor=self.nodeUrl,desired_capabilities=DesiredCapabilities.CHROME)
        except Exception as e:
            print("抛异常了")
            
        # 设置延时
        self.driver.implicitly_wait(30)
        # 浏览器最大化
        self.driver.maximize_window()
        #打开连接    
        self.driver.get(self.url)
        self.fp = open('result/data.txt', mode='a')
    
    def selenium(self):
        lst = []
        lstP = []
        # 找到对象
#         for i in range(20):
# #             print(i+1)
#             l = self.driver.find_element_by_css_selector("#siteHouseList > div:nth-child(%d) > dl > dd:nth-child(2) > p:nth-child(1) > strong > a"%(i+1)).text
#             lst.append(l)
#             time.sleep(1)
#             try:
#                 p = self.driver.find_element_by_xpath('//*[@id="siteHouseList"]/div[%d]/dl/dd[1]/p[5]/span'%(i+1)).text
#             except:
#                 p = self.driver.find_element_by_xpath('//*[@id="siteHouseList"]/div[%d]/dl/dd[1]/p[4]/span'%(i+1)).text
#                 lstP.append(p)
        lst = self.driver.find_elements_by_xpath('//a[@class="c_default f14 mr5"]')
        lstP = self.driver.find_elements_by_xpath('//span[@class="bold c_red"]')

        for name in lst:
#             print(name)
            self.nameList.append(name.text)
            
        for phone in lstP:
#             print(phone)
            self.phoneList.append(phone.text)
            
#         print(self.nameList)
#         print(self.phoneList)
        self.fp.write(str(self.nameList))
        self.fp.write('\n')
        self.fp.write(str(self.phoneList))
        self.fp.write('\n')    
    
    def next(self):
        # 下一页
#         self.driver.find_element_by_id('hlk_next').click()
        self.driver.find_element_by_css_selector('body > div.grid04.w1000.mt10.clearfix > div.colm > div.site-section > div.pl10.pr10.clearfix > div > a.next').click()
    
    def close(self):    
        # 退出
        self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()
    
        
        
if __name__ == '__main__':

    test = SinaAgent()
 
    num = 1118
    for n in range(num):
        print("第%d页开始抓取了！！！！"%(n+1))
        test.fp.write("第%d页开始抓取了！！！！"%(n+1))
        test.fp.write('\n')
        test.selenium()
        if(n+1!=num):
            test.next()
     
#     print(len(test.nameList))
#     print(test.nameList)
#     print(len(test.phoneList))
#     print(test.phoneList)
#     print('名字循环打印开始。。。。。。。。。。。。')
#     for name in test.nameList:
#         print(name)
#       
#     print('电话循环打印开始。。。。。。。。。。。。')   
#     for phone in test.phoneList:
#         print(phone)
    
    test.fp.close() 
    test.close() 
    
    
        
        