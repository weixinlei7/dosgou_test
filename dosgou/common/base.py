from selenium  import  webdriver
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Base():

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElementlocated(self,locator):
        '''定位到元素，返回元素对象，没定位到，返回Timeout异常'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElement(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElements(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            try:
                eles = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_elements(*locator))
                return eles
            except:
                return []

    def sendKeys(self, locator, text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self,locator):
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self,locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            print("没有定位到元素")
            return False
        elif n == 1:
            print("定位到1个元素")
            return True
        else:
            print("定位到多个元素，元素个数为：%s"%n)
            return True

    def is_title(self,_title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text):
        '''返回bool值'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            try:
                result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
                return result
            except:
                return False

    def is_value_in_element(self, locator, _value):
        '''返回bool值，value为空，返回False'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            try:
                result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
                return result
            except:
                return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            element = self.driver.find_element(locator)
            ActionChains(self.driver).move_to_element(element).perform()

    def get_text(self,locator):
        '''获取文本'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            try:
                t = self.findElement(locator).text
                return t
            except:
                print("获取text失败，返回''")
                return ""

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollToView();", target)

    def js_scoll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scoll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get("http://dosgou.testyun.xueyanshe.com/")
    dosgou = Base(driver)
    # loc1 = (By.XPATH, '//div[1]/div/div[2]/a[2]')
    # loc2 = (By.XPATH, '//*[@id="index-login-float"]/div/div[2]/div[1]/div[1]/input[1]')
    # loc3 = (By.XPATH, '//*[@id="index-login-float"]/div/div[2]/div[1]/div[1]/input[2]')
    # loc4 = (By.XPATH, '//*[@id="index-login-float"]/div/div[2]/div[3]')
    loc1 = ("xpath", '//div[1]/div/div[2]/a[2]')
    loc2 = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[1]/div[1]/input[1]')
    loc3 = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[1]/div[1]/input[2]')
    loc4 = ("xpath", '//*[@id="index-login-float"]/div/div[2]/div[3]')
    dosgou.findElement(loc1).click()
    dosgou.sendKeys(loc2,'18614270307')
    dosgou.sendKeys(loc3,'Wei111111')
    dosgou.click(loc4)