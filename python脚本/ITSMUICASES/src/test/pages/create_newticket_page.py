#coding=utf-8
from driver.soudfindelement import findelement
from selenium.webdriver.common.by import By
from src.test.pages.basepage import BasePage
from src.test.pages.base_popwindow_page import PopWindow
import time
class newticket(BasePage,PopWindow):
    def __init__(self,driver):
        self.driver = driver
        self.create_newticket_form_selector = "//div[@id='main']/div/div[@id='layout-content']/div[not(contains(@class,'title'))]/div[@class='ant-spin-container']/div[@class='ticket-wrap']/div[@class='ticket-detail']/div[@class='detail-form']/form[@id='ticketForm']"
        self.find = findelement(self.driver)
    #工单标题
    def set_tickettitle(self,title):
        tickettitle_selector = "title"
        # self.find.findelementbyselector(By.ID,tickettitle_selector).clear()
        # self.find.find_element_visibility_byselector(By.ID,tickettitle_selector,"set tickettitle failed.").send_keys(title)
        self.set_textbox_value(By.ID,tickettitle_selector,title,"set ticket title failed.")
    #工单优先级
    def set_ticketpriority(self,priority):
        ticketpriority_selector ="//label[@for='urgentLevel']/parent::div/following-sibling::div/div/div[@class='ant-radio-group ant-radio-group-large']/label/span[text()='"+priority+"']/preceding-sibling::span/input"
        element =  self.find.find_element_byselector(By.XPATH,ticketpriority_selector,"set ticket priority failed.")
        element.click()
    #输入工单描述
    def set_ticketdescription(self,description):
        ticketdesc_selector = "ticketDesc"
        self.set_textbox_value(By.ID,ticketdesc_selector,description,"set ticket description failed.")
        # self.find.find_element_visibility_byselector(By.ID,ticketdesc_selector).clear()
        # self.find.find_element_visibility_byselector(By.ID,ticketdesc_selector,"set ticket description failed.").send_keys(description)
    #设置创建工单时间
    def set_ticket_createtime(self):
        createtime_input_selector = "//label[@for='startTime']/parent::div/following-sibling::div/div/span/span/input"
        canlendar_confirm_selector =self.create_newticket_form_selector + "//div[@class='ant-calendar-date-panel']/div[@class='ant-calendar-footer']/span/a[@class='ant-calendar-ok-btn']"
        self.find.find_element_visibility_byselector(By.XPATH,createtime_input_selector,"set create newticket time failed.").send_keys("2017-11-20 00:00")
        # self.find.find_elementclickable_byselector(By.XPATH,canlendar_confirm_selector,"canlendar confirm failed.").click()
    #输入创建工单时报告人
    def set_newticket_annoucer(self,annoucer):
        annoucer_selector = "//input[@id='announcer']"
        self.set_textbox_value(By.XPATH,annoucer_selector,annoucer,"set new ticket annoucer failed.")
    #设置事件类型下拉框
    def set_newticket_incidenttype(self,option):
        incidenttype_dropdownlist_selector =self.create_newticket_form_selector + "//label[text()='事件类型']/parent::div/following-sibling::div//div[@class='ant-select-selection__placeholder']"
        incidenttype_options_selector =self.create_newticket_form_selector + "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[text()='"+option+"']"
        self.find.find_element_byselector(By.XPATH,incidenttype_dropdownlist_selector,"incidenttype dropdownlist not visible.").click()
        time.sleep(1)
        self.find.find_element_byselector(By.XPATH,incidenttype_options_selector,"incidenttype option not selected").click()
    #点击提交新建工单按钮
    def commit_newticket_form(self):
        commit_newticket_btn_selector =self.create_newticket_form_selector + "/following-sibling::div/div[@class='ant-row ant-form-item operate']/div[@class='ant-col-offset-3 ant-form-item-label']/button/span"
        self.find.find_element_byselector(By.XPATH,commit_newticket_btn_selector,"commit newticket failed,check commit btn is visible.").click()
    #点击弹出确认提交按钮
    def confirm_commit(self):
        time.sleep(1)
        confirm_selector =self.footer+ ">button.ant-btn.ant-btn-primary.ant-btn-lg>span"
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,confirm_selector,"confirm commit new ticket failed.").click()
    #点击弹出取消提交按钮
    def cancel_commit(self):
        cancel_selector = self.footer+">button.ant-btn.ant-btn-ghost.ant-btn-lg>span"
        self.find.find_element_byselector(By.CSS_SELECTOR,cancel_selector,"cancel commit new ticket failed.").click()






