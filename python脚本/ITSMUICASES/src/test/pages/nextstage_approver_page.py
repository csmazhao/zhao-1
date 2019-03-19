#coding=utf-8
from driver.soudfindelement import findelement
from selenium.webdriver.common.by import By
class nextStage(object):
    def __init__(self,driver):
        self.driver = driver
        self.find = findelement(self.driver)
        self.selectapprover_body_selector = "div.ant-modal-wrap>div.ant-modal.mymodelstyle>div.ant-modal-content>div.ant-modal-body>div.choose-modal>div.choose-user>div.user-tabs>div>div.ant-tabs-content"
        self.approver_window_body_selector = "div.ant-modal-wrap>div.ant-modal.mymodelstyle>div.ant-modal-content>div.ant-modal-body>div.choose-modal"

    def set_user_insearchtextbox(self,value):
        search_user_selector =self.selectapprover_body_selector+ ">div>div>div>div.transfer-list:first-child>div.user-search>span:nth-of-type(2)>input"
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,search_user_selector).clear()
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,search_user_selector).send_keys(value)

    def select_user_insearchresult(self):
        select_user_selector = self.selectapprover_body_selector+">div>div>div>div.transfer-list:first-child>div[style='position:relative;']>ul>li>div>span"
        self.find.find_element_visibility_byselector(By.CSS_SELECTOR,select_user_selector).click()

    def commit_selecteduser(self):
        commit_btn_selector = self.approver_window_body_selector+"div.footer>button:nth-of-type(1)>span"
        self.find.find_elementclickable_byselector(By.CSS_SELECTOR,commit_btn_selector).click()




