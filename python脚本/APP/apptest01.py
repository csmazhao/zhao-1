#! /usr/bin/env python
#coding=utf-8
import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
# from lib2to3.tests.support import driver

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'#设备系统
desired_caps['platformVersion'] = '6.0.1'#设备系统版本
desired_caps['deviceName'] = '小米手机'#设备名称

desired_caps['app'] = PATH('C:\\test\\com.netease.cloudmusic_118.apk')
# desired_caps['appPackage'] = 'com.netease.cloudmusic'
# desired_caps['appActivity'] = 'com.netease.cloudmusic.activity.MainActivity'

#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

time.sleep(5)#启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
driver.find_element_by_css_selector("android.widget.FrameLayout").click()
driver.find_element_by_id('com.netease.cloudmusic:id/a5j').click()
# driver.find_element_by_link_text("【节奏控】那些超带感的音乐（典藏版）").click()
driver.quit()