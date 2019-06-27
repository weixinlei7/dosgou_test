from selenium import  webdriver
import unittest
from pages.login_page import Login
from  pages.free_buy_page import FreeBuy
import time
my = 'http://dosgou.testyun.xueyanshe.com/'

class BuyFreeCrouse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.add_free = FreeBuy(cls.driver)
        a = Login(cls.driver)
        a.login()

    def setUp(self):
        # 每个用例在一个起点
        self.driver.get(my)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_buy_free_crouse(self):
        self.add_free.add_course()
        time.sleep(2)
        self.add_free.in_my_course()
        text = "测试拖拽系列课213123-副本-副本-副本"

        result = self.add_free.judge_course(text)
        print(result)
        self.assertEqual(result, text)


if __name__ == "__main__":
    unittest.main()
