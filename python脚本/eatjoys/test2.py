from selenium import webdriver
from time import sleep
from login_oss.login import login
from login_oss.login import ip
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
####引入chromedriver.exe
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
#####登录
login().user_login(browser)
sleep(2)
browser.refresh()
###########################################################################################################
#######################删除数据#################
print('##########开始删除数据')
######################菜品管理######
print('开始删除菜品')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[6]/span/span[1]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[6]/span/span[1]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
sleep(1)
print('菜品删除成功')
print('删除分类')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[2]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[4]/span/span[1]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('删除分类成功')

#######桌台管理######
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[3]').click()
print('开始删除桌台')
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[6]/span/span[1]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('桌台删除成功')
print('开始删除区域')
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[2]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[3]/span/a').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('区域删除成功')
########员工###########
print('开始删除员工')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[7]/span/span[1]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('员工删除成功')
print('开始删除角色')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[2]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[2]/div/span[1]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('角色删除成功')
###########################################################################################################
###退出
login().user_logout(browser)
print("退出成功")

###关闭浏览器
sleep(5)
login().quit(browser)
print("关闭成功")