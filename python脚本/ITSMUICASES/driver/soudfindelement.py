#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import logging
class findelement(object):
    def __init__(self,driver):
        self.driver = driver
        self.frequency = 0.5
        self.waittime = 5
    def findelementbyselector(self,By,Selector):
        # locator = tag.lower()
        # time.sleep(1)
        # if locator=="id":
        #     element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,selector)))
        # elif locator=="name":
        #     element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.NAME,selector)))
        # elif locator=="class_name":
        #     element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME,selector)))
        # elif locator=="link_text":
        #     element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.LINK_TEXT,selector)))
        # elif locator=="partial_link_text":
        #     element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,selector)))
        # elif locator =="tag_name":
        #     element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.TAG_NAME,selector)))
        # elif locator=="css_selector":
        #     element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,selector)))
        # elif locator =="xpath":
        #     element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,selector)))
        # else:
        #     print "get element failed" #logger
        try:
            for i in range(self.waittime):
                return self.driver.find_element(by=By,value=Selector)
        except NoSuchElementException as Ex:
            print Ex
        # finally:
        #     self.driver.close()

    def findelementsbyselector(self,By,Selector):
        try:
            for i in range(self.waittime):

                return self.driver.find_elements(by=By,value=Selector)
        except NoSuchElementException as Ex:
            print Ex
        # finally:
        #     self.driver.close()

    def find_element_visibility_byselector(self,By,Selector,Msg,Timeout=30):
        try:
            return WebDriverWait(self.driver,Timeout,self.frequency).until(EC.visibility_of_element_located((By,Selector)),Msg)

        except StaleElementReferenceException as Ex:
            print  Ex
        # finally:
        #     self.driver.close()
    #lambda method
    def find_element_byselector(self,By,Selector,Msg,Timeout=30):
        try:
            if By=="xpath":
                return WebDriverWait(self.driver,Timeout,self.frequency).until(lambda T: T.find_element_by_xpath(Selector),Msg)
            elif By=="id":
                return WebDriverWait(self.driver,Timeout,self.frequency).until(lambda T: T.find_element_by_id(Selector),Msg)
            elif By=="css selector":
                return WebDriverWait(self.driver,Timeout,self.frequency).until(lambda T: T.find_element_by_css_selector(Selector),Msg)
            elif By=="tag_name":
                return WebDriverWait(self.driver,Timeout,self.frequency).until(lambda T: T.find_element_by_tag_name(Selector),Msg)
            elif By=="class_name":
                return WebDriverWait(self.driver,Timeout,self.frequency).until(lambda T: T.find_element_by_class_name(Selector),Msg)
            elif By=="name":
                return WebDriverWait(self.driver,Timeout,self.frequency).until(lambda T: T.find_element_by_name(Selector),Msg)
            elif By=="link_text":
                return WebDriverWait(self.driver,Timeout,self.frequency).until(lambda T: T.find_element_by_link_text(Selector),Msg)
            else:
                return  ""
        except NoSuchElementException as Ex:
            print  Ex

    def  find_elements_visibility_byselector(self, By, Selector,Msg, Timeout=30):
        try:
            return WebDriverWait(self.driver,Timeout,self.frequency).until(EC.visibility_of_any_elements_located((By,Selector)),Msg)
        except StaleElementReferenceException as Ex:
            print Ex
        # finally:
        #     self.driver.close()

    def find_element_invisibility_byselector(self,By,Selector,Msg,Timeout=30):
        try:
            return WebDriverWait(self.driver,Timeout,self.frequency).until(EC.invisibility_of_element_located((By,Selector)),Msg)
        except StaleElementReferenceException as Ex:
            print Ex
        # finally:
        #     self.driver.close()

    def find_elementclickable_byselector(self,By,Selector,Msg,Timeout=30):
        try:
            return WebDriverWait(self.driver,Timeout,self.frequency).until(EC.element_to_be_clickable((By,Selector)),Msg)
        except NoSuchElementException as Ex:
            print Ex
        # finally:
        #     self.driver.close()

    def find_element_by_executejs(self,exejs):
        try:
            self.driver.implicitly_wait(3)
            return self.driver.execute_script(exejs)
        except NoSuchElementException as Ex:
            print Ex

    #查询页面已加载dom成功单个元素
    def find_presentedelement_bselector(self,By,Selector,Msg,Timeout=30):
        try:
            return WebDriverWait(self.driver,Timeout,self.frequency).until(EC.presence_of_element_located((By,Selector)),Msg)
        except NoSuchElementException as Ex:
            raise  Ex

    #查询页面已加载dom成功的一组元素
    def find_presentedelements_byselector(self,By,Selector,Msg,Timeout=30):
        try:
            return WebDriverWait(self.driver,Timeout,self.frequency).until(EC.presence_of_all_elements_located((By,Selector)),Msg)
        except NoSuchElementException as Ex:
            print Ex
    #等待页面单个元素出现，出现返回true，否则返回false
    def wait_is_element_visibility(self,By,Selector,Msg,Timeout = 30):
        try:
            WebDriverWait(self.driver,Timeout).until(EC.visibility_of_element_located((By,Selector)),Msg)
            return  True
        except TimeoutException:
            return  False
    #等待页面一组元素出现，出现返回true，否则返回false
    def wait_is_elements_visibility(self,By,Selector,Msg,Timeout = 30):
        try:
            WebDriverWait(self.driver,Timeout).until(EC.visibility_of_all_elements_located((By,Selector)),Msg)
            return  True
        except TimeoutException:
            return False
    #等待页面单个元素消失，消失返回true，否则返回false
    def wait_is_element_invisibility(self,By,Selector,Msg,Timeout = 30):
        try:
            WebDriverWait(self.driver,Timeout).until(EC.invisibility_of_element_located((By,Selector)),Msg)
            return  True
        except TimeoutException:
            return  False
