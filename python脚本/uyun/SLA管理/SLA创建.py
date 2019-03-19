from selenium import webdriver
from time import sleep
from uyun_login.login import login
from uyun_login.login import ip
from selenium.webdriver.common.keys import Keys

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
#####进入服务目录管理
browser.get("%s/itsm/#/conf/sla" %ip)
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.monitor-tabs > span:nth-child(2)").click()
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div.tabs-content > div > header > button").click()
browser.find_element_by_css_selector("#name").send_keys("SLA001")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > form > div:nth-child(2) > div.ant-col-8 > div > div > div > div").click()
sleep(1)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li[1]").click()
browser.find_element_by_css_selector("#sr-time-opt > div > div.ant-col-8 > div > div.ant-select-lg.ant-select.ant-select-enabled.ant-select-allow-clear > div > div").click()
browser.find_element_by_css_selector("#sr-time-opt > div:nth-child(2) > div > div > div > ul > li:nth-child(1) > ul > li").click()
browser.find_element_by_css_selector("#time").send_keys("10")
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > button").click()
