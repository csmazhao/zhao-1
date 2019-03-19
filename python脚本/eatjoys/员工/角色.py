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
print('#############开始测试###########')
###进入员工界面
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]').click()
browser.find_element_by_css_selector('body > div:nth-child(3) > div > div.indexBottom > div.ant-layout > div > div > div.relative > div > div > ul > li:nth-child(2)').click()
###创建角色
browser.find_element_by_css_selector('body > div:nth-child(3) > div > div.indexBottom > div.ant-layout > div > div > div.common-menuContent > div > div > div > div.ant-layout-content > div.roleEstablish > button').click()
browser.find_element_by_css_selector('body > div:nth-child(3) > div > div.indexBottom > div.ant-layout > div > div > div.common-menuContent > div > div > div > div.ant-layout-content > div.roleName > input').send_keys('测试')
browser.find_element_by_css_selector('body > div:nth-child(3) > div > div.indexBottom > div.ant-layout > div > div > div.common-menuContent > div > div > div > div.ant-layout-content > div.CreateARoleBtn > button.ant-btn.ant-btn-primary').click()
###检查创建是否成功
check = browser.find_element_by_css_selector("body > div > div > div.indexBottom > div.ant-layout > div > div > div.common-menuContent > div > div > div > div.ant-layout-content > div.ant-table-wrapper > div > div > div > div > div > table > tbody > tr > td:nth-child(1)").text
try:
    assert check == '测试'
    print("角色创建成功")
except:
    print("创建失败")

###########################################################################################################
###退出
login().user_logout(browser)
print("退出成功")

###关闭浏览器
sleep(5)
login().quit(browser)
print("关闭成功")