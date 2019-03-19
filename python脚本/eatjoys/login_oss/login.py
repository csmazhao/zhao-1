#####用户名和密码#####
user = "18900000009"
passwd = "666666"
ip = "https://oss.eatjoys.cn"

# 设置浏览器需要打开的url

class login():
    def user_login(self, browser):
        browser.get(ip)
        ####等待5S
        browser.implicitly_wait(5)
        browser.maximize_window()

        ######登录
        # browser.find_element_by_xpath('//*[@id="username"]').send_keys(user)
        browser.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[1]/div/div/span/input').send_keys(user)
        browser.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[2]/div/div/span/input').send_keys(passwd)
        # browser.find_element_by_xpath('//*[@id="password"]').send_keys(passwd)
        browser.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[3]/div/div/button').click()
        error = browser.find_element_by_xpath('/html/body/div/div/div[1]/span').text
        try:
            assert error == '食在有趣·商户后台'
            print("登录成功")
        except:
            print("登陆失败")

    def user_logout(self, browser):
        browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/span[4]/i').click()

    def quit(self, browser):
        browser.quit()