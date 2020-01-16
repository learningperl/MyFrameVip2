# coding=utf8
from selenium import webdriver
from common.logger import logger
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, os,traceback


# 浏览器操作的类
class Web:
    """
    打开并操作浏览器的类
    """

    def __init__(self, w):
        self.driver = None
        self.writer = w

    def openbrowser(self, b='chrome', d='chromedriver'):
        if b == 'chrome' or b == "":
            if d == "":
                d = "chromedriver"

            op = Options()
            # 去掉提示条
            op.add_argument('--disable-infobars')
            # 添加用户配置文件，可以带缓存
            try:
                userdir = os.environ['USERPROFILE'] + "\\AppData\\\Local\\\Google\\\Chrome\\User Data"
            except Exception as e:
                userdir = 'C:\\Users\\Will\\AppData\\Local\\Google\\Chrome\\User Data'

            op.add_argument('--user-data-dir=' + userdir)
            self.driver = webdriver.Chrome(executable_path=d, options=op)
            self.driver.implicitly_wait(30)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "成功打开浏览器")

    def geturl(self, url):
        self.driver.get(url)
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, str(url))

    def click(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "点击成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def input(self, xpath, text):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(text)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "输入成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def iniframe(self, xpath):
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "输入成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def outiframe(self, xpath):
        try:
            self.driver.switch_to().default_content()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "输入成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def switchwindow(self,index):
        try:
            self.driver.switch_to.window(self.driver.window_handles[int(index)])
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "输入成功")

        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))


    def moveto(self,xpath):
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.driver.find_element_by_xpath(xpath)).perform()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "输入成功")

        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def excutejs(self, js):
        """
        封装了默认执行js的方法
        :param js: 需要执行的标准js语句
        :return: 无
        """
        try:
            self.driver.execute_script(js)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            # 定位失败，则直接返回
            return False