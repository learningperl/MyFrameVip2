# -*- coding: UTF-8 -*-
import unittest,os
from selenium import webdriver


# 创建一个测试类，继承unittest
class MyTest(unittest.TestCase):

    # 类变量，保存浏览器
    driver = None

    # 初始化
    @classmethod
    def setUpClass(cls):
        print('初始化\n')
        option = webdriver.ChromeOptions()
        # 去掉提示条的配置
        option.add_argument('disable-infobars')
        # 获取用目录
        try:
            # 异常处理，如果获取到，就使用获取到路径
            userdir = os.environ['USERPROFILE']
        except Exception as e:
            # 如果没有获取到，就使用默认的Administrator路径
            # 打印异常信息
            # traceback.print_exc()
            userdir = 'C:\\Users\\Administrator'

        userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
        userdir = '--user-data-dir=' + userdir
        # 添加用户目录
        option.add_argument(userdir)
        cls.driver = webdriver.Chrome(executable_path='../lib/chromedriver.exe',options=option)
        # 设置默认等待时间
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # 结束
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('执行完成')

    # 首页
    def test_index(self):
        print('首页')
        self.driver.get('http://112.74.191.10:8000/index.php')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]').click()

        self.driver.find_element_by_xpath('/html/body/div[11]/div[1]/div/div/div[2]/a[1]').click()

    # 登录
    def test_login(self):
        print('登录')
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('13800138006')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('1111')
        self.driver.find_element_by_xpath('//div[@class="login_bnt"]/a')
        self.driver.find_element_by_xpath('//div[@class="login_bn111t"]/a')


if __name__ == '__main__':
    unittest.main()
