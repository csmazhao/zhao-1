import ConfigParser
import os.path
from selenium import webdriver
class Config(object):
    chrome_path = os.path.dirname(os.path.abspath('..//..//'))+"\\resource\chromedriver.exe"
    ie_path=""
    firefox_path=""
    # def __init__(self,driver):
    #     self.driver = driver
    def openbrowse(self):
        conf = ConfigParser.ConfigParser()
        configfiledir = os.path.dirname(os.path.abspath('..//..//'))+"\config\option.ini"
        conf.read(configfiledir)
        browser = conf.get("browser","name")
        url = conf.get("host","url")
        if browser.lower()=="chrome":
            option = webdriver.ChromeOptions()
            option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            driver = webdriver.Chrome(executable_path=self.chrome_path,chrome_options=option)
            #webdriver.ChromeOptions()
        elif browser.lower()=="ie":
            driver = webdriver.Ie(self.ie_path)
        elif browser.lower()=="firefox":
            driver = webdriver.Firefox(self.firefox_path)
        else:
            driver = None
        driver.implicitly_wait(5)
        driver.get(url)
        driver.maximize_window()
        return driver
    def quitbrowse(self):
        self.driver.quit()





