#coding=utf-8
from selenium import webdriver
from driver.soudfindelement import findelement
from selenium.webdriver.common.by import By
class dataList(object):
    def __init__(self,driver):
        self.driver = driver
        self.datalist_body_xpath = "//div[@id='main']/div/div[@id='layout-content']/div[@class='content-wrap']/div[@class='ticket-main']/div[@id='ticket-list-wrap']/div/div[@class='ticket-list-mian']/div[@class='ticket-table-wrap']"
        self.find = findelement(self.driver)
    def getsinglerowdata(self):
        self.datalist_body_css = "div#main>div>div#layout-content>div.content-wrap>div.ticket-main>div.ticket-list-wrap>div>div.ticket-list-mian"
    #切换视图
    def switch_to_view(self):
        view_button_css = "div#filter>div.menu>div.filter.clearfix>div.filter-rg>div>button.ant-btn.ant-btn-primary.ant-btn-icon-only.active"
        self.find.find_elementclickable_byselector(By.CSS_SELECTOR,view_button_css).click()
    #打开工单列表中符合条件的单条工单
    def link_singleticket_in_datalist(self,ticketname,stage):
        # self.switch_to_view()
        groupofticket_selector =self.datalist_body_xpath + "/ul[@class='ticket-list']/li/ul/li[3]/span[2][text()='"+stage+"']/parent::li/parent::ul/preceding-sibling::div/a/span[text()='"+ticketname+"']/parent::a"
        tickets =  self.find.find_elements_visibility_byselector(By.XPATH,groupofticket_selector)
        for ticket in tickets:
            if (ticket != None):
                ticket.click()
                break






