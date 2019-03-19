#coding=utf-8
from selenium.webdriver.common.by import By
from driver.soudfindelement import findelement
class modelManage(object):
    def __init__(self,driver):
        self.driver = driver
        self.find = findelement(self.driver)
        self.title = "//div[@id='layout-content']/div[@class='title.rela']"
        self.body = "//div[@id='layout-content']/div[@class='content-wrap']/div[@class='config-main']/div/div[@class='model-squares']/div/div[@class='ant-spin-container']/div[@class='model-card-wrap']/div[@class='clearfix model-cards']"
    def new_model_btn(self):
        create_btn_selector =self.body + "/div/div[@class='model_top']/button[@type='button']/span"
        self.find.find_elementclickable_byselector(By.XPATH,create_btn_selector,"link model manage menu failed.").click()
    #切换视图
    def switch_to_view(self):
        view_js = """
        (function(){
            var view_btns = document.getElementsByTagName('button');
                for (var i = 0;i<view_btns.length;i++)
                    {
                        cls = view_btns[i].getAttribute('class');
                        if (cls.indexOf('ant-btn ant-btn-primary ant-btn-icon-only') > -1 && cls.indexOf('active') > -1)
                        {
                            view_btns[i].click();
                        }
                    }
                })();"""
        self.find.find_element_by_executejs(view_js)
    def switch_model_using(self,model_name):
        start_model_selector = self.body + "/div/div/div/a/h3[contains(text(),'"+model_name+"')]/parent::a/following-sibling::span/span"
        self.find.find_element_visibility_byselector(By.XPATH,start_model_selector,"model not exsit.").click()
    def copy_model(self,model_name):
        copy_model_selector = self.body + "/div/div/div/a/h3[contains(text(),'"+model_name+"')]/parent::a/following-sibling::div/span/button[@class='ant-btn sqcopy']/span"
        self.find.find_element_visibility_byselector(By.XPATH,copy_model_selector,"copy model btn not exist.").click()




