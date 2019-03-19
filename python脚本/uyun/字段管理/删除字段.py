from selenium import webdriver
from time import sleep
from uyun_login.login import login
from uyun_login.login import ip

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

#引入chromedriver.exe
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

##登录
login().user_login(browser)
print("登录成功")
sleep(2)

###进入字段管理中
browser.get("%s/itsm/#/conf/field" %ip)

###删除字段
for i in range(2, 18):
    sleep(2)
    browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.uy-table-td-href > span > a.href-btn.warning").click()
sleep(3)


sleep(2)

##删除字段分组

browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr > td.uy-table-td-href > a > i").click()
browser.implicitly_wait(5)
browser.find_element_by_link_text("删除").click()
sleep(3)
###退出
login().user_logout(browser)
print("退出成功")

###关闭浏览器
sleep(5)
login().quitt(browser)
print("关闭成功")