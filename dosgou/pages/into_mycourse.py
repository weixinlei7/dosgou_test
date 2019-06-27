# coding:utf-8
from selenium  import  webdriver
from common.base import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait

class Mycourse(Base):     # 继承Base
    # 进入我的学习

    loc_my = ("xpath", '//*[@class="user_name"]/span')
    loc_my_in = ("xpath", '//*[@class="study"]/span')

    def in_my_course(self,):
        time.sleep(2)
        mouse = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.loc_my))
        ActionChains(self.driver).move_to_element(mouse).perform()
        self.click(self.loc_my_in)





