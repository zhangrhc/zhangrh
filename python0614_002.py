#coding=utf-8
'''
cnblog的登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确（还有用户名和密码均为空时与此情况是一样的，这里就不单独测试了）
'''

import unittest
from selenium import webdriver
from time import sleep

class LoginCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    #定义登录方法
    def login(self, username, password):
        self.dr.get('https://passport.cnblogs.com/user/signin')  #cnblog登录页面
        self.dr.find_element_by_id('input1').send_keys(username)
        self.dr.find_element_by_id('input2').send_keys(password)
        self.dr.find_element_by_id('signin').click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('kemi_xxx', 'kemi_xxxx') #正确用户名和密码
        sleep(3)
        link = self.dr.find_element_by_id('lnk_current_user')
        self.assertTrue('菜鸟可米' in link.text)   #用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里
        self.dr.get_screenshot_as_file("D:\cnblogtest\\login_success.jpg")  #截图  可自定义截图后的保存位置和图片命名

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('kemi_xxx', 'kemi')  #正确用户名，错误密码
        sleep(2)
        error_message = self.dr.find_element_by_id('tip_btn').text
        self.assertIn('用户名或密码错误', error_message)  #用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        self.dr.get_screenshot_as_file("D:\cnblogtest\\login_pwd_error.jpg")

    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('kemi_xxx', '')  #密码为空
        error_message = self.dr.find_element_by_id('tip_input2').text
        self.assertEqual(error_message,'请输入密码')  #用assertEqual(a,b)方法来断言  a == b  请输入密码等于error_message
        self.dr.get_screenshot_as_file("D:\cnblogtest\\login_pwd_null.jpg")

    def test_login_user_error(self):
        '''用户名错误、密码正确'''
        self.login('kemixing', 'kemi_xxx')  #密码正确，用户名错误
        sleep(2)
        error_message = self.dr.find_element_by_id('tip_btn').text
        self.assertIn('该用户不存在', error_message)  #用assertIn(a,b)方法来断言 a in b
        self.dr.get_screenshot_as_file("D:\cnblogtest\\login_user_error.jpg")

    def test_login_user_null(self):
        '''用户名为空、密码正确'''
        self.login('', 'kemi_xxx')  #用户名为空，密码正确
        error_message = self.dr.find_element_by_id('tip_input1').text
        self.assertEqual(error_message,'请输入登录用户名')  #用assertEqual(a,b)方法来断言  a == b
        self.dr.get_screenshot_as_file("D:\cnblogtest\\login_user_null.jpg")

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()