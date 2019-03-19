#coding=utf-8
from src.test.common.login import login
from src.test.common.globals import glv
import unittest
from src.test.pages.leftnavigation_page import leftmenu
from src.test.pages.datalist_page import dataList
from src.test.pages.ticket_approve_page import ApprovePage
class secondlineapprove(unittest.TestCase):

    def test_secondlineapprove(self):
        admin = login(name=glv.gl_admin,pasword=glv.gl_adminpas)
        self.driver = login.userlogin(admin)
        navigation = leftmenu(self.driver)
        navigation.link_my_todo()
        data = dataList(self.driver)
        approve = ApprovePage(self.driver)
        data.link_singleticket_in_datalist(glv.gl_new_ticket_name,"二线处理")
        approve.submit_ticket()
        approve.confirm_commit()

    if __name__ == "__main__":
        unittest.main()

