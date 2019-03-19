from selenium import webdriver
from time import sleep
from uyun_login.login import login
from uyun_login.login import ip
# from calculator import count
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
# import unittest
####引入chromedriver.exe
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

#####登录
login().user_login(browser)
sleep(2)

#####进入字段管理中
browser.get("%s/itsm/#/conf/field" %ip)
# #####创建字段分组
# browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button:nth-child(1)").click()
# browser.find_element_by_css_selector("#name").send_keys("test")
# browser.find_element_by_css_selector("body > div:nth-child(11) > div > div.uy-modal-wrap > div > div.uy-modal-content > div.uy-modal-footer > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
# sleep(2)
###########进入字段界面
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
########################
################################################
#################################单行文本字段#######################################
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(1) > div").click()
################字段名为空校验

browser.find_element_by_css_selector("#code").send_keys("dhwb")
##分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#name").send_keys()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
error = browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(1) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div").text
try:
    assert error  == '请输入字段名'
    print("当字段名为空时，测试通过")
except:
    print("当字段名为空时，测试失败")

sleep(2)
browser.find_element_by_css_selector("#name").send_keys("sddddddddddddddddddddddddd")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
error = browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(1) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div").text
try:
    assert error  == '最多输入15个字符'
    print("当大于字段限制15长度时，测试通过")
except:
    print("当大于字段限制15长度时，测试失败")

sleep(2)
browser.find_element_by_css_selector("#name").clear()
browser.find_element_by_css_selector("#name").send_keys("    ")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
sleep(1)
error = browser.find_element_by_css_selector("body > div:nth-child(12) > div > span > div > div > div > span").text
try:
    assert error  == '字段名称长度不符合限定(32字符)'
    print("当字段名为空格时，测试通过")
except:
    print("当字段名为空格时，测试失败")



########################################################################
################################################
########################
# ###删除字段
# browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()
# browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-1 > td.uy-table-td-href > span > a.href-btn.warning").click()
#
# sleep(2)
#
# ###删除字段分组
#
# browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr > td.uy-table-td-href > a > i").click()
# browser.implicitly_wait(5)
# browser.find_element_by_link_text("删除").click()
# # sleep(3)
# # ###退出
# login().user_logout(browser)
# print("退出成功")
#
# ###关闭浏览器
# sleep(10)
# login().quitt(browser)
# print("关闭成功")