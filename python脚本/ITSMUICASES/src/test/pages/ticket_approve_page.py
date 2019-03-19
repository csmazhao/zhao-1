#coding=utf-8
from driver.soudfindelement import findelement
from selenium.webdriver.common.by import By
from src.test.pages.base_popwindow_page import PopWindow
import time
class ApprovePage(PopWindow):
    def __init__(self,driver):
        self.driver = driver
        self.find = findelement(self.driver)
        #工单编辑页面#####################################
        #工单编辑页面导航栏标题CSS
        self.ticket_edit_nav_title = "div#main>div>div#layout-content>div.title.rela"
        #工单编辑页面form css
        self.ticket_edit_form = "div#main>div>div#layout-content>div.ticket-wrap>div.ticket-edit.ticket-detail>div.detail-form"
        #操作按钮
        self.ticket_operation_btn = ">div.detail-btn>div>div>div>div>div>div>"
        self.js_confirm_btn = """
    (function(){
    var btns = document.getElementsByTagName('button');
    for(var i = 0;i<btns.length;i++)
    {
        if (btns[i].className=='ant-btn ant-btn-primary ant-btn-lg')
        {
            if(btns[i].clientHeight != 0 && btns[i].clientWidth != 0)
            {
                btns[i].click();
                break;
            }
        }
    }})();"""

    def set_content_in_textarea(self,value):
        # w = webdriver.Chrome()
        # w.find_element_by_css_selector().send_keys()
        textarea_css = self.ticket_edit_form+">form#ticketForm>div:nth-of-type(9)>div:last-child>div>span>textarea"
        time.sleep(1)
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,textarea_css).clear()
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,textarea_css).send_keys(value)
    def accept_ticket(self):
        accept_btn_css = self.ticket_edit_form+self.ticket_operation_btn+"button:nth-of-type(1)>span"
        time.sleep(1)
        self.find.find_elementclickable_byselector(By.CSS_SELECTOR,accept_btn_css).click()

    def submit_ticket(self):
        submit_btn_css =self.ticket_edit_form+self.ticket_operation_btn+"button:nth-of-type(1)>span"
        self.find.find_elementclickable_byselector(By.CSS_SELECTOR,submit_btn_css).click()
    #完成提交窗体中点击确定按钮
    def confirm_commit(self):
        self.find.find_element_by_executejs(self.js_confirm_btn)
    #完成提交窗体中点击下个审批人文本框
    def select_nextapprover_inuserlist(self):
        select_userlist_selector = self.body + ">form>div:nth-of-type(1)>div:nth-of-type(2)>div>div#userList"
        self.find.find_elementclickable_byselector(By.CSS_SELECTOR,select_userlist_selector)
    #完成提交窗体中设置处理意见
    def set_approveadvise_in_finishcommit_window(self,handlerAdvise):
        approveadvise_selector = self.body+ ">form>div:nth-of-type(2)>div:nth-of-type(2)>div>div>div:nth-of-type(1)>div>textarea.mention-input__input"
        time.sleep(1)
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,approveadvise_selector).clear()
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,approveadvise_selector).send_keys(handlerAdvise)















