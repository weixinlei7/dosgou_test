# coding:utf-8
from selenium  import  webdriver
from common.base import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait

class JudgCourse(Base):     # 继承Base
    # 判断免费课程已购买

    loc_new = ("xpath", '//*[@id="userclass_list"]/div[1]/div[2]/h4/a')

    def judge_course(self, _text):
        return self.is_text_in_element(self.loc_new, _text)



