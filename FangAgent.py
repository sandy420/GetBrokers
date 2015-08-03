#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class FangAgent(object):

    def __init__(self):
        #成都
        self.url = 'http://esf.cd.fang.com/agenthome/-h30-i31-j310/'
        #重庆
        self.url = 'http://esf.xj.fang.com/agenthome/ '
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
        
#         self.fp = open('result/fang.txt', mode='w')
    
    def selenium(self):
        time.sleep(1)
        # 找到housetitle
        lst = self.driver.find_elements_by_css_selector("#houseRow_0_43474169 > div.house > dl > dt > p.housetitle > a")
        lstP = self.driver.find_elements_by_xpath('//p[@class="black"]/strong')

        for name in lst:
#             print(name.text)
            self.nameList.append(name.text)
            
        for phone in lstP:
#             print(phone.text)
            self.phoneList.append(phone.text)
            
#         print(self.nameList)
#         print(self.phoneList)
#         self.fp.write(str(self.nameList))
#         self.fp.write('\n')
#         self.fp.write(str(self.phoneList))
#         self.fp.write('\n')  
    
    def next(self):
        # 下一页
        self.driver.find_element_by_id('hlk_next').click()
    
    def close(self):    
        # 退出
        self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()
    
        
        
if __name__ == '__main__':

    test = FangAgent()
 
    num = 59
    for n in range(num):
        print("第%d页开始抓取了！！！！"%(n+1))
#         test.fp.write("第%d页开始抓取了！！！！"%(n+1))
#         test.fp.write('\n')
        test.selenium()
        if(n+1!=num):
            test.next()
     
    print(len(test.nameList))
    print(test.nameList)
    print(len(test.phoneList))
    print(test.phoneList)
    print('名字循环打印开始。。。。。。。。。。。。')
    for name in test.nameList:
        print(name)
     
    print('电话循环打印开始。。。。。。。。。。。。')   
    for phone in test.phoneList:
        print(phone) 
     
    test.close()