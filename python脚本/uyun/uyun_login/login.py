#####用户名和密码#####
user = "mazhao010@broada.com"
passwd = "Mazhao@123"
ip = "http://10.1.11.254"

# 设置浏览器需要打开的url
url = "%s/tenant/#/login_admin"
urlout ="%s/tenant/#/logout"

class login():
    def user_login(self, browser):
        browser.get(url %ip)
        ####等待5S
        browser.implicitly_wait(5)
        browser.maximize_window()

        ######登录
        browser.find_element_by_css_selector("#email").click()
        browser.find_element_by_css_selector("#email").send_keys(user)
        browser.find_element_by_id("passwd").click()
        browser.find_element_by_id("passwd").send_keys(passwd)
        browser.find_element_by_css_selector("#code").click()
        browser.find_element_by_css_selector("#code").send_keys("uyun")
        ######进入ITSM界面
        browser.find_element_by_css_selector("#main > div > div.login.clearfix.login.login_office > form > div.ant-col-14.ant-col-offset-7 > div > button").click()
        browser.implicitly_wait(5)
        browser.find_element_by_css_selector("#main > div > ul > li:nth-child(2)").click()

    def user_logout(self, browser):
        browser.get(urlout %ip)

    def quitt(self, browser):
        browser.quit()