#coding=utf-8
from driver.soudfindelement import findelement
from src.test.pages import basepage
from src.test.pages import base_popwindow_page
from src.test.common.globals import glv
from selenium.webdriver.common.by import By
import time
class newmodel(basepage.BasePage,base_popwindow_page.PopWindow):
    def __init__(self,driver):
        self.driver = driver
        self.find = findelement(self.driver)
        self.newmodel_form_selector = "div#main>div>div#layout-content>div.content-wrap>div.model-main>div.config-main.edit-page"
        self.basic_info = ">div.model-form-section.basic-info>form"
        self.process_set = ">div.model-form-section.process-set>form"
        self.action = ">div.action>form"
        self.form_xpath = "//div[@id='main']/div/div[@id='layout-content']/div[@class='content-wrap']/div[@class='model-main']/div[@class='config-main edit-page']/div[@class='model-form-section basic-info']"
    def set_newmodel_name(self):
        newmodel_name_selector = self.newmodel_form_selector+self.basic_info+ ">div:nth-of-type(1)>div>div>span>input"
        self.set_textbox_value(By.CSS_SELECTOR,newmodel_name_selector,glv.gl_model_name,"set model name failed.")
    def set_newmodel_prefix(self):
        newmodel_prefix_selector = self.newmodel_form_selector+self.basic_info + ">div:nth-of-type(2)>div:nth-of-type(2)>div>div:nth-of-type(1)>div>div>div>span>input"
        self.set_textbox_value(By.CSS_SELECTOR,newmodel_prefix_selector,glv.gl_model_gdgz,"set model gdgz failed.")
    def set_newmodel_gdgzdate(self,date):
        newmodel_datedrp_selector = self.form_xpath + "/form/div/div/label[text()='工单规则']/parent::div/following-sibling::div/div/div[2]/div/div/div/div/div/div/div[2]"
        newmodel_dateopt_selector = self.form_xpath + "/div[1]/div/div/div/ul/li[contains(text(),'"+date+"')]"
        self.set_dropdownlist_options(By.XPATH,newmodel_datedrp_selector,newmodel_dateopt_selector,"set gdgz date failed.")
    def set_newmodel_gdgz_flowno(self,flowno):
        newmodel_flowdrp_selector = self.form_xpath + "/form/div/div/label[text()='工单规则']/parent::div/following-sibling::div/div/div[3]/div/div/div/div/div/div/div[2]"
        newmodel_flowopt_selector = self.form_xpath + "/div[2]/div/div/div/ul/li[contains(text(),'"+flowno+"')]"
        self.set_dropdownlist_options(By.XPATH,newmodel_flowdrp_selector,newmodel_flowopt_selector,"set gdgz flowno failed.")
    def set_newmodel_description(self,description):
        newmodel_modeldesc_selector = self.newmodel_form_selector + self.basic_info + ">div:nth-of-type(3)>div:nth-of-type(2)>div>span>textarea"
        self.set_textbox_value(By.CSS_SELECTOR,newmodel_modeldesc_selector,description,"set model description failed.")
    def set_newmodel_admin(self,model_admin):
        newmodel_adminbtn_selector = self.newmodel_form_selector +self.basic_info+ ">div:nth-of-type(5)>div:nth-of-type(2)>div>button>span"
        newmodel_admin_selectuserinput_selector = self.body + ">div.choose-modal>div.choose-user>div.user-list>div.user-search>span>input"
        newmodel_admin_selectuser_link_selector = self.body+ ">div.choose-modal>div.choose-user>div.user-list>ul>li>label>span:nth-of-type(1)"
        newmodel_admin_appenduserbtn_selector = self.body+">div.choose-modal>div.choose-user>ul.operate>p.seperate>button>span"
        newmodel_commit_adminuser_selected_selector = self.body + ">div.choose-modal>div.footer>button>span"
        self.find.find_element_byselector(By.CSS_SELECTOR,newmodel_adminbtn_selector,"assign new model admin failed").click()
        self.set_textbox_value(By.CSS_SELECTOR,newmodel_admin_selectuserinput_selector,model_admin,"input admin user in the pop window failed")
        time.sleep(1)
        self.find.find_element_byselector(By.CSS_SELECTOR,newmodel_admin_selectuser_link_selector,"select admin user in the search result failed.").click()
        self.find.find_element_byselector(By.CSS_SELECTOR,newmodel_admin_appenduserbtn_selector,"add admin user failed.").click()
        self.find.find_element_byselector(By.CSS_SELECTOR,newmodel_commit_adminuser_selected_selector,"commit selected admin user failed.").click()

    #设置创建模型基本信息
    def set_newmodel_basicinfo(self):
        pass









