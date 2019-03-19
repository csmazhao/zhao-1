#coding=utf-8
from driver.soudfindelement import findelement
import time
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.find = findelement(self.driver)
    def set_textbox_value(self, By, Selector, Value, Msg, Timeout=10):
        self.find.find_element_visibility_byselector(By,Selector,Msg,Timeout).clear()
        self.find.find_element_visibility_byselector(By,Selector,Msg,Timeout).send_keys(Value)
    def set_dropdownlist_options(self,By,Selector1,Selector2,Msg,Timeout=10):
        self.find.find_element_visibility_byselector(By,Selector1,Msg,Timeout).click()
        time.sleep(1)
        self.find.find_element_visibility_byselector(By,Selector2,Msg,Timeout).click()



