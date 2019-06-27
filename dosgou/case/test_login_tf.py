from selenium import webdriver
import unittest
from pages.login_page import Login,url
import time
import ddt
from common.read_excel import ExcelUtil
import os

'''
1.输入18614270307，密码Wei111111，登录
2.输入18614270307，密码 登录
3.输入 密码Wei111111 登录
'''

testdatas = [
            {"user":"18614270307","pwd":"Wei111111","expection":True},
            {"user":"18614270307","pwd":"","expection":False},
            {"user":"111","pwd":"Wei111111","expection":False},
            ]

# propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# filepath = os.path.join(propath,"ke17","datas.xlsx")
# print(filepath)
# data = ExcelUtil(filepath)  # filepath, sheetName
# testdatas = data.dict_data()
# print (testdatas)

@ddt.ddt
class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.login_page = Login(cls.driver)
        cls.driver.maximize_window()


    def setUp(self):
        # self.driver.get(url)
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(2)

    def login_case(self,user,pwd,expection):
        self.login_page.login(user,pwd)
        time.sleep(2)
        result = self.login_page.get_login_result(user)
        print("测试结果：%s" % result)
        self.assertTrue(result == expection)

    @ddt.data ( *testdatas)
    def test_01(self,data):
        '''登录测试用例'''
        print('\n','-------------------开始测试---------------------')
        print("测试数据”%s" % data)
        self.login_case(data["user"],data["pwd"],data["expection"])
        print('-------------------结束测试---------------------')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

