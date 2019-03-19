#coding=utf-8
from driver.soudfindelement import findelement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
class Logout:
    def __init__(self,driver):
        self.driver = driver
        self.find = findelement(self.driver)
    def do_logout(self):
        logout_userlabel_selector = "header#header>ul#user-info>li.user-li>a>span"
        signout_selector = "header#header>ul#user-info>li.user-li>ul#user-box>li:last-child>a"
        ActionChains(self.driver).move_to_element(self.find.find_element_byselector(By.CSS_SELECTOR,logout_userlabel_selector,"can not find user label.")).perform()
        self.find.find_element_byselector(By.CSS_SELECTOR,signout_selector,"user logout failed.").click()
        print "logout success..."



