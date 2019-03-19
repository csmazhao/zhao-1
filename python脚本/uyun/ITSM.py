from selenium import webdriver
from login.login import login
import os

#引入chromedriver.exe
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

##登录
login().user_login(browser)
print("登录成功")
#sleep(10)

#退出
login().user_logout(browser)
print("退出成功")

#关闭浏览器
#sleep(10)
login().quitt(browser)
print("关闭成功")