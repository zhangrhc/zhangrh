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
        self.dr.find_element_by_id("username").clear()
        self.dr.find_element_by_id('username').send_keys(username)
        #对于隐藏的元素，需要先调用js修改元素为可见，才可以进行操作
        self.dr.execute_script("document.getElementById('password').style.display='block';")
        self.dr.find_element_by_id("password").clear()
        self.dr.find_element_by_id('password').send_keys(password)
        self.dr.find_element_by_id('loginBtn').click()


    def test_validate_button(self):
        '''用户名、密码正确'''
        self.login('admin', 'ufsoft123') #正确用户名和密码
        sleep(2)
        link=self.dr.find_element_by_xpath("//span[@class='snavbtn btn-nav-work-default-alt btn-nav-work-default-first']").text
        self.assertTrue('机构版系统管理' in link)   #用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里
        self.dr.get_screenshot_as_file("D:\\cnblogtest\\validate_button_success.jpg")  #截图  可自定义截图后的保存位置和图片命名
        sleep(2)
        '''
        self.dr.find_element_by_xpath("//span[@translate='ISM_FUN_13']").click()
        sleep(1)
        #打开新建工作日志界面
        self.dr.find_element_by_xpath("//span[@translate='FUN_BT_66']").click()
        sleep(1)
        #为各个字段赋值，有默认值的使用默认值。
        #为各个字段赋值，有默认值的使用默认值。由于send_key默认是utf-8所以必须把汉字转换成unicode，用函数decode()
        self.dr.find_element_by_xpath("//a[@class='select2-choice select2-default']").click()
        sleep(1)
        #为a标签这种通过js实现的
        self.dr.find_element_by_xpath("//div[@class='select2-result-label']").click()
        sleep(2)
        #获取当前的日期时间，并转换成字符串，因为send_keys函数中必须用字符串
        t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #为各个字段赋值，有默认值的使用默认值。由于send_key默认是utf-8所以必须把汉字转换成unicode，用函数decode()
        self.dr.find_element_by_id('worklogTime4').send_keys((u"自动测试工作日志",t))
        self.dr.find_element_by_xpath("//textarea[@ng-model='worklog.work_solution']").send_keys(('自动测试工作日志').decode())
        #为下拉列表选择值，以下两条是录制脚本导出为python脚本后，拷贝出来的，不好取的元素可以使用这种方法取。但是通过js创建的控件是不能通过录制定位到元素的
        Select(self.dr.find_element_by_xpath("//select[@ng-model='worklog.service_way']")).select_by_visible_text(u"远程")
        Select(self.dr.find_element_by_xpath("//select[@ng-model='worklog.access_control']")).select_by_visible_text(u"本机构可见")
        sleep(2)
        self.dr.find_element_by_xpath("//button[@translate='FUN_BT_35']").click()
        #由于提交后要跳转才能搜索到新的页面中元素，必须加sleep(3)以上
        sleep(3)
        success_text=self.dr.find_element_by_xpath("//p[@style='overflow: hidden;white-space: nowrap;-o-text-overflow:ellipsis;text-overflow: ellipsis;']").text
        self.assertIn(t, success_text)  #用assertIn(a,b)方法来断言 a in b
        self.dr.get_screenshot_as_file("D:\\cnblogtest\\daily_log_success.jpg")
    '''

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit()

if __name__ == '__main__':
    #unittest.main()
    LoginCase()
