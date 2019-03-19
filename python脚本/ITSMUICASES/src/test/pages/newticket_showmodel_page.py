#coding=utf-8
from src.test.common.globals import glv
from driver.soudfindelement import findelement
from selenium.webdriver.common.by import By
class showmodel(object):
    def __init__(self,driver):
        self.driver = driver
        self.showmodel_body_selector = "//div[@class='ant-modal-wrap add-ticket-service-modal']/div[@class='ant-modal']/div[@class='ant-modal-content']/div[@class='ant-modal-body']"
        self.find = findelement(self.driver)
    #点击弹窗模型窗体中指定模型
    def select_model_in_showmodel_window(self):
        modelname_selector = self.showmodel_body_selector+"/div/form/div/div/div/div/div[text()='"+glv.gl_model_name+"']"
        self.find.find_elementclickable_byselector(By.XPATH,modelname_selector,15).click()





