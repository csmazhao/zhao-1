#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from driver.soudfindelement import findelement
class leftmenu():
    def __init__(self,driver):
        self.driver = driver
        #左边树形菜单
        self.left_nav_menu_css = "div#main>div>aside#left-panel>div.panel-wrap>div.panel>nav#nav"
        self.find = findelement(self.driver)
    #我的待办链接
    def link_my_todo(self):
        mytodo_css =self.left_nav_menu_css + ">ul:nth-of-type(1)>li:nth-of-type(2)>a>span:nth-of-type(1)"
        WebDriverWait(self.driver,5).until(lambda X: X.find_element_by_css_selector(mytodo_css),"link my todo left menu failed.").click()
    #我参与过的链接
    def link_my_participate(self):
        mypart_css =self.left_nav_menu_css + ">ul:nth-of-type(1)>li:nth-of-type(4)>a>span:nth-of-type(1)"
        WebDriverWait(self.driver,5).until(lambda X: X.find_element_by_css_selector(mypart_css),"link my participate left menu failed.").click()
    #所有工单链接
    def link_alldata(self):
        alldata_css =self.left_nav_menu_css + ">ul:nth-of-type(1)>li:nth-of-type(5)>a>span:nth-of-type(1)"
        WebDriverWait(self.driver,5).until(lambda X: X.find_element_by_css_selector(alldata_css),"link all data left menu failed.").click()
    #我的关注链接
    def link_my_follow(self):
        myfollow_css =self.left_nav_menu_css + ">ul:nth-of-type(1)>li:nth-of-type(5)>a>span:nth-of-type(1)"
        WebDriverWait(self.driver,5).until(lambda X: X.find_element_by_css_selector(myfollow_css),"link my follow left menu failed.").click()
    #获取我的待办数量
    def get_mytodo_count(self):
        mytodo_count_css =self.left_nav_menu_css + ">ul:nth-of-type(1)>li:nth-of-type(2)>a>span.menu-item-badge>span"
        return WebDriverWait(self.driver,5).until(lambda X: X.find_element_by_css_selector(mytodo_count_css),"get my todo count failed.").text

    #获取我的关注数量
    def get_myfollw_count(self,myfollow_count=""):
        myfollow_count_css =self.left_nav_menu_css + ">ul:nth-of-type(1)>li:nth-of-type(3)>a>span.menu-item-badge>span"
        return WebDriverWait(self.driver,5).until(lambda X: X.find_element_by_css_selector(myfollow_count_css),"get my follow count failed.").text

    #获取我参与过的数量
    def get_myparticipate_count(self):
        myparticipate_count_css = self.left_nav_menu_css + ">ul:nth-of-type(1)>li:nth-of-type(4)>a>span.menu-item-badge>span"
        return WebDriverWait(self.driver,5).until(lambda X: X.find_element_by_css_selector(myparticipate_count_css),"get my participate count failed.").text

    #配置项菜单####################################
    def link_model_mange(self):
        modelmanage_css =self.left_nav_menu_css + ">ul:nth-of-type(2)>li:nth-of-type(1)>a>span"
        WebDriverWait(self.driver,5).until(lambda X: X.find_element_by_css_selector(modelmanage_css),"link model manage menu failed.").click()
    #工单##########################################
    def link_create_newticket(self):
        newticket_btn_selector = self.left_nav_menu_css+">div:nth-of-type(1)>button>span"
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,newticket_btn_selector,"click create ticket button failed").click()



