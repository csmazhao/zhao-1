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
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button:nth-child(1)").click()
browser.find_element_by_css_selector("#name").send_keys("test")
browser.find_element_by_css_selector("body > div:nth-child(11) > div > div.uy-modal-wrap > div > div.uy-modal-content > div.uy-modal-footer > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
sleep(2)
########################
################################################
print("#############开始创建字段啦####################")
print("#############开始创建字段啦####################")
print("#############开始创建字段啦####################")
#################################单行文本字段#######################################
dh_name = "Auto单行文本"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(1) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %dh_name)
browser.find_element_by_css_selector("#code").send_keys("dhwb")
##分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()
# browser.find_element_by_link_text("test").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %dh_name)
print("%s**************创建成功" %dh_name)
sleep(2)
########################################################################
#################################多行文本字段#######################################
ddh_name = "Auto多行文本"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(2) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("ddhwb")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()
###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
##检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################下拉菜单#######################################
ddh_name = "Auto下拉菜单"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(3) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("xlcd")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()
###添加自定义值
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(2) > div.uy-col-15 > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div:nth-child(1) > div.uy-col-21 > button").click()
sleep(1)
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(2) > div.uy-col-15 > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div:nth-child(1) > div.uy-col-21 > button").click()
###添加值
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(2) > div.uy-col-15 > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div:nth-child(2) > div.uy-col-21 > span.item-label > input").send_keys("下拉值1")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(2) > div.uy-col-15 > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div:nth-child(2) > div.uy-col-21 > span.item-value > input").send_keys("1")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(2) > div.uy-col-15 > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div:nth-child(3) > div.uy-col-21 > span.item-label > input").send_keys("下拉值2")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(2) > div.uy-col-15 > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div:nth-child(3) > div.uy-col-21 > span.item-value > input").send_keys("2")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(2) > div.uy-col-15 > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div:nth-child(4) > div.uy-col-21 > span.item-label > input").send_keys("下拉值3")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(2) > div.uy-col-15 > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div:nth-child(4) > div.uy-col-21 > span.item-value > input").send_keys("3")
###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div > div:nth-child(3) > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################单选#######################################
ddh_name = "Auto单选"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(4) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("dx")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()
###添加自定义值
browser.find_element_by_css_selector("#params > button").click()
sleep(1)
browser.find_element_by_css_selector("#params > button").click()
###添加值
browser.find_element_by_css_selector("#params > div > div:nth-child(1) > span.item-label > input").send_keys("单选值1")
browser.find_element_by_css_selector("#params > div > div:nth-child(1) > span.item-value > input").send_keys("1")
browser.find_element_by_css_selector("#params > div > div:nth-child(2) > span.item-label > input").send_keys("单选值2")
browser.find_element_by_css_selector("#params > div > div:nth-child(2) > span.item-value > input").send_keys("2")
browser.find_element_by_css_selector("#params > div > div:nth-child(3) > span.item-label > input").send_keys("单选值3")
browser.find_element_by_css_selector("#params > div > div:nth-child(3) > span.item-value > input").send_keys("3")

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################多选#######################################
ddh_name = "Auto多选"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(5) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("ddx")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()
###添加自定义值
browser.find_element_by_css_selector("#params > button").click()
sleep(1)
browser.find_element_by_css_selector("#params > button").click()
###添加值
browser.find_element_by_css_selector("#params > div > div:nth-child(1) > span.item-label > input").send_keys("单选值1")
browser.find_element_by_css_selector("#params > div > div:nth-child(1) > span.item-value > input").send_keys("1")
browser.find_element_by_css_selector("#params > div > div:nth-child(2) > span.item-label > input").send_keys("单选值2")
browser.find_element_by_css_selector("#params > div > div:nth-child(2) > span.item-value > input").send_keys("2")
browser.find_element_by_css_selector("#params > div > div:nth-child(3) > span.item-label > input").send_keys("单选值3")
browser.find_element_by_css_selector("#params > div > div:nth-child(3) > span.item-value > input").send_keys("3")

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################整数#######################################
ddh_name = "Auto整数"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(6) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("zs")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################整数1#######################################
ddh_name = "Auto整数1"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(6) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("zss")
browser.find_element_by_css_selector("#defaultValue").send_keys("25")
browser.find_element_by_css_selector("#unit").send_keys("美元")
browser.find_element_by_css_selector("#intMin").send_keys("10")
browser.find_element_by_css_selector("#intMax").send_keys("90")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)

########################################################################
#################################小数#######################################
ddh_name = "Auto小数"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(7) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("xs")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()
###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################小数1#######################################
ddh_name = "Auto小数1"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(7) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("xss")
browser.find_element_by_css_selector("#defaultValue").send_keys("0.25")
browser.find_element_by_css_selector("#unit").send_keys("吨吨吨吨吨")
browser.find_element_by_css_selector("#precision").send_keys("2")
browser.find_element_by_css_selector("#doubleMin").send_keys("0.01")
browser.find_element_by_css_selector("#doubleMax").send_keys("9.99")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################时间日期#######################################
ddh_name = "Auto时间日期"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(8) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("sjrq")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################时间日期1#######################################
ddh_name = "Auto时间日期1"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(8) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("sjrqq")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(5) > div.uy-col-15.uy-form-item-control-wrapper > div > div > label:nth-child(2) > span.uy-radio > input").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(6) > div.uy-col-15.uy-form-item-control-wrapper > div > div > label.uy-radio-wrapper.uy-radio-wrapper-checked > span.uy-radio.uy-radio-checked > input").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(7) > div.uy-col-15.uy-form-item-control-wrapper > div > label > span.uy-checkbox > input").click()
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)

########################################################################
#################################人员#######################################
ddh_name = "Auto人员"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(9) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("ry")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################人员1#######################################
ddh_name = "Auto人员1"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(9) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("ryy")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div.uy-row.uy-form-item > div.uy-col-15.uy-form-item-control-wrapper > div > label > span.uy-checkbox > input").click()
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################部门#######################################
ddh_name = "Auto部门"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(10) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("bm")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################部门1#######################################
ddh_name = "Auto部门1"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(10) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("bmm")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div.uy-row.uy-form-item > div.uy-col-15.uy-form-item-control-wrapper > div > label > span.uy-checkbox > input").click()
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
########################################################################
#################################富文本#######################################
ddh_name = "Auto富文本"
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.field-list-filter.clearfix > span.operation-btns > button.uy-btn.uy-btn-primary.uy-btn-lg").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-header-wrap > div > div.uy-col-21.uy-form-item-control-wrapper > div > ul > li:nth-child(10) > div").click()
browser.find_element_by_css_selector("#name").send_keys("%s" %ddh_name)
browser.find_element_by_css_selector("#code").send_keys("fwf")
###分组选择
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div:nth-child(1) > div:nth-child(2) > div > div.uy-col-15.uy-form-item-control-wrapper > div > div > div > div").click()
browser.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li").click()

###保存
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.field-layout > div.uy-row > div.uy-col-15 > div > button:nth-child(1)").click()
###检查字段
#browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr.uy-table-row.uy-table-row-level-0 > td:nth-child(1) > span.uy-table-row-expand-icon.uy-table-row-collapsed").click()browser.find_element_by_link_text("%s" %ddh_name)
print("%s**************创建成功" %ddh_name)
sleep(2)
print("#############创建成功啦####################")
print("#############创建成功啦####################")
print("#############创建成功啦####################")

sleep(2)
browser.refresh()
################################################################################################
# ##############删除字段

print("#############开始删除啦####################")
print("#############开始删除啦####################")
print("#############开始删除啦####################")
###删除字段
sleep(5)
for i in range(2, 18):
    sleep(2)
    browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.uy-table-td-href > span > a.href-btn.warning").click()
sleep(3)
print("#############删除字段成功####################")
##删除字段分组

browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.uy-tabs-content.uy-tabs-content-no-animated > div.uy-tabs-tabpane.uy-tabs-tabpane-active > div > div.uy-table-wrapper > div > div > div > div > div > table > tbody > tr > td.uy-table-td-href > a > i").click()
browser.implicitly_wait(5)
browser.find_element_by_link_text("删除").click()
sleep(3)
print("#############删除字段组成功####################")
###退出
login().user_logout(browser)
print("退出成功")

###关闭浏览器
sleep(5)
login().quitt(browser)
print("关闭成功")