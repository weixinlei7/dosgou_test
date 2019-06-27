# coding:utf-8
from selenium  import  webdriver
from common.base import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait

url ='http://dosgou.testyun.xueyanshe.com/'
class Login(Base):     # 继承Base
    # 定位登陆

    loc_click_login = ("xpath", '//*[@class="top_loginout"]/a[2]')
    loc_user = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[1]/div[1]/input[1]')
    loc_pwd = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[1]/div[1]/input[2]')
    loc_button = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[3]')
    loc_go_team = ("link text", "机构登录")
    loc_forget_pwd = ("xpath",'//*[@id="index-login-float"]/div/div[2]/p[2]/a[2]')
    loc_get_user = ("xpath",'//*[@class="myname"]')
    loc_forget_pwd_page = ("xpath", '//*[@id="index-login-findPwd"]/div/div[1]')

    def click_login(self):
        self.click(self.loc_click_login)

    def input_user(self, text = "18614270307"):
        self.sendKeys(self.loc_user, text)

    def input_pwd(self, text = "Wei111111"):
        self.sendKeys(self.loc_pwd,text)

    def click_button(self):
        self.click(self.loc_button)

    def go_team(self):
        self.click(self.loc_go_team)

    def forget_pwd(self):
        self.click(self.loc_forget_pwd)

    def get_login_name(self):
        user = self.get_text(self.loc_get_user)
        return user

    def get_login_result(self,user):
        result = self.is_text_in_element(self.loc_get_user,user)
        return result

    def max_windows(self):
        self.driver.maximize_window()

    def login(self,user='18614270307', pwd='Wei111111' ):  # keep_login=False
        '''登陆流程'''
        self.driver.get(url)
        self.click_login()
        self.input_user(user)
        self.input_pwd(pwd)
        # if keep_login: self.click_keep_login()
        self.click_button()

    def is_exist(self):
        '''判断忘记密码页，“忘记密码”是否存在'''
        r = self.isElementExist(self.loc_forget_pwd_page)
        return r


if __name__ == "__main__":
    driver = webdriver.Chrome()
    login_page = Login(driver)
    login_page.login()
    # driver.get(url)
    # driver.maximize_window()
    # login_page.click_login()
    # login_page.input_user("18614270307")
    # login_page.input_pwd("Wei111111")
    # login_page.go_team()
    # login_page.forget_pwd()

