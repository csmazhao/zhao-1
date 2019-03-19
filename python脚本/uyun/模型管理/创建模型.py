from selenium import webdriver
from time import sleep
from test1 import login
from test1 import ip
from selenium.webdriver.common.action_chains import ActionChains
import os

#引入chromedriver.exe
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

##登录
login().user_login(browser)
print("登录成功")
sleep(2)

###进入模型管理中
browser.get("%s/itsm/#/conf/model" %ip)

##新建模型分组
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.field-list-filter-group.uy-btn-primary.uy-btn-lg").click()

browser.find_element_by_css_selector("#name").send_keys("test")
#确定创建
browser.find_element_by_css_selector("body > div:nth-child(11) > div > div.uy-modal-wrap > div > div.uy-modal-content > div.uy-modal-footer > button.uy-btn.uy-btn-primary.uy-btn-lg").click()

sleep(3)
#新建事件模型
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.add-model.uy-btn-primary.uy-btn-lg > span").click()
sleep(2)
browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div/div[1]").click()
sleep(3)
###输入参数
browser.find_element_by_css_selector("#model-basic-info > form > div:nth-child(6) > div.ant-col-12 > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div.action > button:nth-child(1)").click()
##启动模型
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.model-list-table > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(4) > span").click()
sleep(3)
###停止模型
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.model-list-table > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(4) > span").click()
sleep(2)
###删除模型
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.model-list-table > div:nth-child(2) > div > div:nth-child(2) > div > div.clearfix.model-list-row-operate > div.fl.delete").click()
sleep(3)
#browser.find_element_by_css_selector("body > div:nth-child(14) > div > div.uy-modal-wrap > div > div.uy-modal-content > div > div > div.uy-confirm-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()

browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button[2]").click()

sleep(3)
###删除模型组
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.model-list-table > div:nth-child(2) > div > div.model-list-group-operate.clearfix > div.model-list-group-operate-pos > i").click()
sleep(3)
# browser.find_element_by_css_selector("body > div:nth-child(12) > div > div > ul > li:nth-child(2)").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[2]").click()




sleep(3)
###退出
login().user_logout(browser)
print("退出成功")

###关闭浏览器
sleep(3)
login().quitt(browser)
print("关闭成功")