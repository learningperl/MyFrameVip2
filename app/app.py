# coding:utf8

import time, os,traceback,threading
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from common.logger import logger

# 浏览器操作的类
class APP:
    """
    打开并操作浏览器的类
    """

    def __init__(self, w):
        self.driver = None
        self.writer = w
        self.h = '4723'

    def startappium(self,c='', h='4723', t='5'):
        # 启动的命令行
        def run(cmd):
            os.system(cmd)

        self.h = h

        cmd = 'node "' + c + '" -p ' + h
        print(cmd)
        # 用线程th执行函数run
        th = threading.Thread(target=run, args=(cmd,))
        th.start()
        time.sleep(int(t))
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1,'启动appium成功')

    def startapp(self, jsonparma, t='10'):
        conf = eval(jsonparma)
        # 连接appium并启动APP
        self.driver = webdriver.Remote("http://127.0.0.1:"+self.h+"/wd/hub", conf)
        self.driver.implicitly_wait(20)
        time.sleep(int(t))
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, '启动APP成功')

    def __find_element(self, locator):
        time.sleep(5)
        """
        内部用来查找元素的方法
        支持使用三种主流查找方式
        :param locator: 支持输入xpath，id，content-desc
        :return:
        """
        try:
            if locator.find(':id') > -1:
                ele = self.driver.find_element_by_id(locator)
            else:
                if locator.startswith('/'):
                    ele = self.driver.find_element_by_xpath(locator)
                else:
                    ele = self.driver.find_element_by_accessibility_id(locator)
        except Exception as e:
            logger.exception(e)
            return None
        return ele

    def click(self, xpath):
        try:
            ele = self.__find_element(xpath)
            ele.click()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "点击成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def input(self, xpath, text):
        try:
            ele = self.__find_element(xpath)
            ele.send_keys(text)
            self.writer.write(self.writer.row, self.writer.clo + 1, "输入成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def moveto(self,locator):
        try:
            lo = eval(locator)
            TouchAction(self.driver).press(x=lo[0], y=lo[1]).move_to(x=lo[2], y=lo[3]).release().perform()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "输入成功")

        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def sleep(self,t='5'):
        time.sleep(int(t))
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, "等待完成")

    def close(self):
        os.system('taskkill /F /IM node.exe')
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, "已退出appium")





