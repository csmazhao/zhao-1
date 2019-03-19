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
browser.get("%s/itsm/#/conf/catlog" %ip)

####创建服务目录
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.catlog-left > div > div.create-btn-warp > button").click()
browser.find_element_by_css_selector("#name").send_keys("AutoMuLu")
browser.find_element_by_css_selector("#catlog-form-item > form > div:nth-child(2) > div.ant-col-12 > div > span > span > span.ant-select-selection__rendered").click()
browser.implicitly_wait(5)
browser.find_element_by_link_text("根节点").click()
browser.find_element_by_css_selector("#isShow").click()
browser.find_element_by_css_selector("#serviceDirDetail > div.service-item > div.service-save-wrap > button").click()

sleep(3)
#####创建第二个目录
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.catlog-left > div > div.create-btn-warp > button").click()
browser.find_element_by_css_selector("#name").send_keys("AutoMuLu2")
browser.find_element_by_css_selector("#catlog-form-item > form > div:nth-child(2) > div.ant-col-12 > div > span > span > span.ant-select-selection__rendered").click()
browser.implicitly_wait(5)
browser.find_element_by_css_selector("#catlog-form-item > div > div > div > div > ul > li:nth-child(2) > a > span").click()
browser.find_element_by_css_selector("#isShow").click()
browser.find_element_by_css_selector("#serviceDirDetail > div.service-item > div.service-save-wrap > button").click()

####给第一个目录创建服务指引项
browser.find_element_by_css_selector("#layout-content > div.content-wrap > div > div > div > div.catlog-left > div > div.tree-menu-wrap > div > ul > li > a > span > div").click()
browser.find_element_by_css_selector("#serviceDirDetail > div.service-item > div.service-title-wrap > div.service-item-head.clearfix > div.service-item-btn > button:nth-child(2)").click()
sleep(3)
####选择服务指引
browser.find_element_by_css_selector("#ticketForm > div.service-mode > div > div.ant-tabs.ant-tabs-top.service-model-tabs.ant-tabs-line > div.ant-tabs-bar > div > div > div > div > div:nth-child(3)").click()
# browser.find_element_by_css_selector("#ticketForm > div.service-mode > div > div.ant-tabs.ant-tabs-top.service-model-tabs.ant-tabs-line > div.ant-tabs-bar > div > div > div > div").send_keys(Keys.ARROW_RIGHT)


browser.find_element_by_css_selector("#ticketForm > div.service-mode > div > div.ant-tabs.ant-tabs-top.service-model-tabs.ant-tabs-line > div.ant-tabs-content > div > div:nth-child(2) > div > div > div > div.simditor-wrapper > div.simditor-body").send_keys("auto_test")
browser.find_element_by_css_selector("#name").send_keys("autoFWX")
browser.find_element_by_css_selector("#code").send_keys("autocode")
browser.find_element_by_css_selector("#tel_num").send_keys("autotest")
browser.find_element_by_css_selector("#recommend").click()
browser.find_element_by_css_selector("#online").click()
browser.find_element_by_css_selector("#ticketForm > form.ant-form.ant-form-horizontal.service-scenar > div > div.ant-col-12 > div > div.ant-radio-group.ant-radio-group-large > label:nth-child(2)").click()
browser.find_element_by_css_selector("#sr-time-opt > form > div > div.ant-col-12 > div > div.ant-select-lg.ant-select.ant-select-enabled.ant-select-allow-clear > div > div > div").click()
browser.find_element_by_css_selector("#sr-time-opt > div > div > div > div > ul > li:nth-child(1) > ul > li").click()
browser.find_element_by_css_selector("#tags-lists").click()
sleep(2)
browser.find_element_by_css_selector("body > div:nth-child(13) > div > div.uy-modal-wrap > div > div.uy-modal-content > div > div > div.choose-user > div > div > div.ant-tabs-content > div > div > div > div:nth-child(1) > div:nth-child(2) > ul > li:nth-child(1)").click()
browser.find_element_by_css_selector("body > div:nth-child(13) > div > div.uy-modal-wrap > div > div.uy-modal-content > div > div > div.choose-user > div > div > div.ant-tabs-content > div > div > div > div:nth-child(1) > div:nth-child(2) > ul > li").click()
browser.find_element_by_css_selector("body > div:nth-child(13) > div > div.uy-modal-wrap > div > div.uy-modal-content > div > div > div.footer > button:nth-child(1)").click()
sleep(2)
browser.find_element_by_css_selector("#ticketForm > div.fixed-bottom > button").click()