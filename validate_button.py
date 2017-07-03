# coding=utf-8

#以下三行，解决UnicodeDecodeError: 'utf8' codec can't decode byte 0xb0 in position 35: invalid
#start 报错
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.support.select import Select

class LoginCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    #定义登录方法
    def login(self, username, password):
        self.dr.get('http://172.20.17.153:9080/portal/login.html?lrid=1')  #cnblog登录页面
        self.dr.find_element_by_id('username').clear()
        self.dr.find_element_by_id('username').send_keys(username)
        #对于隐藏的元素，需要先调用js修改元素为可见，才可以进行操作
        self.dr.execute_script("document.getElementById('password').style.display='block';")
        self.dr.find_element_by_id('password').clear()
        self.dr.find_element_by_id('password').send_keys(password)
        self.dr.find_element_by_id('loginBtn').click()


    def test_validate_button(self):
        '''用户名、密码正确'''
        self.login('admin', 'ufsoft123') #正确用户名和密码
        sleep(2)
        link=self.dr.find_element_by_xpath("//span[@class='snavbtn btn-nav-work-default-alt btn-nav-work-default-first']").text
        self.assertTrue('机构版系统管理' in link)   #用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里
        self.dr.get_screenshot_as_file("D:\\cnblogtest\\validate_button_success.jpg")  #截图  可自定义截图后的保存位置和图片命名
        sleep(1)
        #选择平行的两组元素中第二个，所有的li标签id='pmng_admin'中第二个。机构版档案对照验证
        self.dr.find_element_by_xpath("//li[2][@id='pmng_admin']/a/span").click()
        sleep(1)
        link1=self.dr.find_element_by_id('0001ZZ1000000001RYH5').text
        self.assertTrue('机构档案对照' in link1)
        #工作日志权限控制验证
        self.dr.find_element_by_xpath("//li[3][@id='pmng_admin']/a/span").click()
        sleep(1)
        link2=self.dr.find_element_by_id('0001ZZ1000000001SK2V').text
        self.assertTrue('工作日志权限控' in link2)
        #域帐号预置权限验证
        self.dr.find_element_by_xpath("//li[4][@id='pmng_admin']/a/span").click()
        sleep(1)
        link3=self.dr.find_element_by_id('0001ZZ1000000001QKBK').text
        self.assertTrue('域帐号预置权限' in link3)
        #自动验证规则设置
        self.dr.find_element_by_xpath("//li[5][@id='pmng_admin']/a/span").click()
        sleep(1)
        link3=self.dr.find_element_by_id('0001ZZ1000000001SWFA').text
        self.assertTrue('自动验证规则设' in link3)

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit()

if __name__ == '__main__':
    #unittest.main()
    LoginCase()
