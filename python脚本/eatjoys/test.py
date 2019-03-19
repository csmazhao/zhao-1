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
print('###########员工##################')
# ###进入员工界面
# browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]').click()
# browser.find_element_by_css_selector('body > div:nth-child(3) > div > div.indexBottom > div.ant-layout > div > div > div.relative > div > div > ul > li:nth-child(2)').click()
# ###创建角色
# ###创建角色
# browser.find_element_by_css_selector('body > div:nth-child(3) > div > div.indexBottom > div.ant-layout > div > div > div.common-menuContent > div > div > div > div.ant-layout-content > div.roleEstablish > button').click()
# browser.find_element_by_css_selector('body > div:nth-child(3) > div > div.indexBottom > div.ant-layout > div > div > div.common-menuContent > div > div > div > div.ant-layout-content > div.roleName > input').send_keys('测试')
# browser.find_element_by_css_selector('body > div:nth-child(3) > div > div.indexBottom > div.ant-layout > div > div > div.common-menuContent > div > div > div > div.ant-layout-content > div.CreateARoleBtn > button.ant-btn.ant-btn-primary').click()
# ###检查创建是否成功
# check = browser.find_element_by_css_selector("body > div > div > div.indexBottom > div.ant-layout > div > div > div.common-menuContent > div > div > div > div.ant-layout-content > div.ant-table-wrapper > div > div > div > div > div > table > tbody > tr > td:nth-child(1)").text
# try:
#     assert check == '测试'
#     print("角色创建成功")
# except:
#     print("角色创建失败")
# #######创建员工
# #######创建员工
# browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
# browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button').click()
# browser.find_element_by_xpath('//*[@id="employeeName"]').send_keys('自动化测试员工')
# browser.find_element_by_xpath('//*[@id="iPhone"]').send_keys('18900000020')
# browser.find_element_by_xpath('//*[@id="employeeNo"]').send_keys('001')
# browser.find_element_by_xpath('//*[@id="post"]').send_keys('自动化测试职务')
# browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[5]/div[2]/div/span/div/input').click()
# browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[6]/div[2]/div/div/label[2]').click()
# browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[7]/div[2]/div/div/label').click()
# browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[8]/div/div/button[2]').click()
# ###检查创建是否成功
# check = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]').text
# try:
#     assert check == '自动化测试员工'
#     print("员工创建成功")
# except:
#     print("员工创建失败")
# print('#############桌台###############')
# #######进入桌台管理
# browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[1]/ul/li[3]').click()
# sleep(2)
# #######创建区域
# browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[2]').click()
# browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/button').click()
# browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/p[1]/input').send_keys('大堂')
# browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/p[2]/input').send_keys('1')
# sleep(2)
# browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[3]/button[2]').click()
# ###检查创建是否成功
# check = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[1]/span[2]').text
# try:
#     assert check == '大堂'
#     print("区域创建成功")
# except:
#     print("区域创建失败")
# sleep(4)
# ######创建桌台
# browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
# browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button').click()
# browser.find_element_by_xpath('//*[@id="deskName"]').send_keys('自动化测试桌台')
# browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[2]/div[2]/div/div').click()
# sleep(2)
# browser.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li').click()
# browser.find_element_by_xpath('//*[@id="deskLimit"]').send_keys('5')
# browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[8]/div[2]/div/div/label[2]').click()
# browser.find_element_by_xpath('//*[@id="shortUrl"]').send_keys('qwerty')
# browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[9]/div/div/button[1]').click()
# ###检查创建是否成功
# check = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[1]').text
# try:
#     assert check == '自动化测试桌台'
#     print("桌台创建成功")
# except:
#     print("桌台创建失败")
# print('#############菜品###############')
####进入菜品管理
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[1]/ul/li[4]').click()
####创建分类
sleep(2)
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[2]').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/button').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="categoryName"]').send_keys('测试菜品分类')
browser.find_element_by_xpath('//*[@id="sort"]').send_keys('1')
browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/div/button[1]').click()
###检查创建是否成功
check = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/span[2]').text
try:
    assert check == '测试菜品分类'
    print("菜品分类创建成功")
except:
    print("菜品分类创建失败")
####创建菜品
sleep(2)
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
sleep(2)
####创建简易菜品
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button').click()
browser.find_element_by_xpath('//*[@id="dishesName"]').send_keys('简易菜品')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div/div').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[4]/div[2]/div/div/div/div').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
sleep(2)
# browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[5]/div[2]/div/div/div/div').click()
sleep(2)
# browser.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()
# sleep(2)
browser.find_element_by_xpath('//*[@id="salePrice"]').send_keys('20')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[7]/div/div/button[1]').click()
###检查创建是否成功
check = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[1]').text
try:
    assert check == '简易菜品'
    print("简易菜品创建成功")
except:
    print("简易菜品创建失败")
####创建高级模式-单一价格菜品
sleep(2)
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button').click()
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div/label[2]').click()
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/input').send_keys('高级菜品-单一价格')
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/div/div/div').click()

sleep(2)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[4]/div/div/div').click()

sleep(2)
browser.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[1]').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[5]/input').send_keys('gjcp')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/input').send_keys('25')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/input').send_keys('15')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/button').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[1]/input').send_keys('小料01')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[2]/input').send_keys('5')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[3]/input').send_keys('3')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/button').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[1]/input').send_keys('小料02')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/input').send_keys('6')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[3]/input').send_keys('2')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/button').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[4]/div/div[1]/input').send_keys('100')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/input').send_keys('50')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[4]/div/div[3]/input').send_keys('10')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[4]/div/div[5]/input').send_keys('50')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/button[2]').click()
sleep(2)
###检查创建是否成功
check = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[1]').text
try:
    assert check == '高级菜品-单一价格'
    print("高级菜品-单一价格菜品创建成功")
except:
    print("高级菜品-单一价格菜品创建失败")
###########################################################################
print('##########开始删除数据')
browser.refresh()
sleep(2)
######################菜品管理######
print('开始删除菜品')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[6]/span/span[1]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[6]/span/span[1]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
sleep(2)
print('菜品删除成功')
print('删除分类')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[2]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[4]/span/span[1]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('删除分类成功')

#######桌台管理######
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[3]').click()
print('开始删除桌台')
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[6]/span/span[1]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('桌台删除成功')
print('开始删除区域')
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[2]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/table/tbody/tr/td[3]/span/a').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('区域删除成功')
########员工###########
print('开始删除员工')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[7]/span/span[1]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('员工删除成功')
print('开始删除角色')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[2]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[2]/div/span[1]').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
print('角色删除成功')
print('数据删除成功')
###########################################################################################################
##退出
login().user_logout(browser)
print("退出成功")

###关闭浏览器
sleep(5)
login().quit(browser)
print("关闭成功")
