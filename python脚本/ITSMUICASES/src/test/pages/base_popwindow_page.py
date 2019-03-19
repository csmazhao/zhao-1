#coding=utf-8
class PopWindow(object):
    header = "div.ant-modal-wrap:not([style='display: none;'])>div[class^='ant-modal']>div.ant-modal-header"
    body = "div.ant-modal-wrap:not([style='display: none;'])>div[class^='ant-modal']>div.ant-modal-content>div.ant-modal-body"
    footer = "div.ant-modal-wrap:not([style='display: none;'])>div[class^='ant-modal']>div.ant-modal-content>div.ant-modal-footer"
    body_xpath = ""
    def __init__(self,driver):
        self.driver = driver
        #div.ant-modal-wrap>div.ant-modal.finish-submit




