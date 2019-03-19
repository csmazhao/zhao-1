#coding=utf-8
import unittest
from src.test.common.login import login
from src.test.pages.ticket_approve_page import ApprovePage
from src.test.pages.leftnavigation_page import leftmenu
from src.test.pages.datalist_page import dataList
from src.test.pages.nextstage_approver_page import nextStage
from selenium.webdriver.support.ui import WebDriverWait
from src.test.common.globals import glv
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC
import time
class approveticket(unittest.TestCase):

    def test_approveickets(self):
        admin = login(name=glv.gl_admin,pasword=glv.gl_adminpas)
        self.driver = login.userlogin(admin)
        approve = ApprovePage(self.driver)
        leftnav =leftmenu(self.driver)
        datalist =dataList(self.driver)
        nextstage = nextStage(self.driver)
        leftnav.link_my_todo()
        datalist.link_singleticket_in_datalist(glv.gl_new_ticket_name,"一线处理")
        #accept ticket
        approve.accept_ticket()
        #solution
        approve.set_content_in_textarea("solution")
        #submit
        approve.submit_ticket()
        #select approver and submit
        approve.select_nextapprover_inuserlist()
        #search user
        nextstage.set_user_insearchtextbox("admin")
        #select user
        nextstage.select_user_insearchresult()
        # commit selected user
        nextstage.commit_selecteduser()
        #input agree
        approve.set_approveadvise_in_finishcommit_window("agree")
        #commit approver
        approve.confirm_commit()

        if __name__=="__main__":
            unittest.main()


        




