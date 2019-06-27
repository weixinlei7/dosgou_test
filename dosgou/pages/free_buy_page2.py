# coding:utf-8
from selenium  import  webdriver
from common.base import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait

class FreeBuy(Base):     # 继承Base
    # 定位登陆

    loc1 = ("xpath", '//div[1]/div/div[2]/a[2]')
    loc2 = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[1]/div[1]/input[1]')
    loc3 = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[1]/div[1]/input[2]')
    loc4 = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[3]')

    # 加入免费课程

    loc_course_in = ("xpath", "/html/body/include/div[2]/ul/div/div[1]/li[2]/a")
    loc_course = ("xpath", '//*[@id="class_list"]/div[1]/div[2]/p/a')
    loc_add_free = ("xpath", '//*[@class="ci-top-left"]/a[1]/span')

    # 判断免费课程已购买

    loc_my = ("xpath", '//*[@class="user_name"]/span')
    loc_my_in = ("xpath", '//*[@class="study"]/span')
    loc_new = ("xpath", '//*[@id="userclass_list"]/div[1]/div[2]/h4/a')

    def login(self, user='18614270307', pwd='Wei111111'):
        self.driver.get("http://dosgou.testyun.xueyanshe.com/")
        self.driver.maximize_window()
        self.click(self.loc1)
        self.sendKeys(self.loc2, user)
        self.sendKeys(self.loc3, pwd)
        self.click(self.loc4)

    def add_course(self):
        time.sleep(2)
        self.click(self.loc_course_in)
        time.sleep(2)
        self.click(self.loc_course)
        time.sleep(2)
        self.click(self.loc_add_free)

    def in_my_course(self,):
        time.sleep(2)
        mouse = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.loc_my))
        ActionChains(self.driver).move_to_element(mouse).perform()
        self.click(self.loc_my_in)

    def judge_course(self, _text):
        return self.is_text_in_element(self.loc_new, _text)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    add_free = FreeBuy(driver)
    add_free.login()
    add_free.add_course()
    add_free.in_my_course()
    text = "测试课程视频3423"
    result = add_free.judge_course(text)
    print(result)
    if result is True:
        print("课程购买成功!")
    else:
        print("课程购买失败!")


