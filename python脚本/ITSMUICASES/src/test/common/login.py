#coding=utf-8
from config.config import Config
from driver.soudfindelement import findelement
from selenium.webdriver.common.by import By
from src.test.pages.basepage import BasePage
class login(BasePage):
    def __init__(self,name='',pasword=''):
        self.name = name
        self.pasword = pasword
        config = Config()
        self.driver = config.openbrowse()
        self.find = findelement(self.driver)
    def userlogin(self):
        self.set_textbox_value(By.ID,"email",self.name,"input username failed.")
        itsm_menu_locator = "//div[@id='main']/div/div[@class='list']/div[@class='manage']/ul/li/p[text()='ITSM']"
        login_commit_selector = "div#main>div.login-box>div.login.clearfix.login.login_office>form>div:nth-of-type(2)>div>button[type='submit']"
        self.set_textbox_value(By.ID,"passwd",self.pasword,"input user pass failed.")
        self.find.find_element_byselector(By.CSS_SELECTOR,login_commit_selector,"user login failed.").click()
        self.find.find_element_byselector(By.XPATH,itsm_menu_locator,"open itsm menu failed.").click()
        self.driver.implicitly_wait(5)
        return self.driver

