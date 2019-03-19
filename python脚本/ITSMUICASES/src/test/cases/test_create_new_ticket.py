#coding=utf-8
import unittest
from src.test.common.login import login
from src.test.common.globals import glv
from src.test.pages.leftnavigation_page import leftmenu
from src.test.pages.newticket_showmodel_page import showmodel
from src.test.pages.create_newticket_page import newticket
"""
author: kanghs
date:2017-11-10
function:创建事件工单
"""
class createnewticket(unittest.TestCase):
    def test_createnewtickets(self):
        admin =login(name=glv.gl_admin,pasword=glv.gl_adminpas)
        self.driver = login.userlogin(admin)
        navigation = leftmenu(self.driver)
        navigation.link_create_newticket()
        model = showmodel(self.driver)
        model.select_model_in_showmodel_window()
        createticket = newticket(self.driver)

        createticket.set_tickettitle(glv.gl_new_ticket_name)
        # WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"title")),"set ticket title failed").send_keys("title")
        createticket.set_ticketpriority("极高")
        createticket.set_ticketdescription("create_new_incident_ticket_desc")
        createticket.set_ticket_createtime()
        createticket.set_newticket_annoucer(glv.gl_new_ticket_requester)
        createticket.set_newticket_incidenttype("软件")
        createticket.commit_newticket_form()
        createticket.confirm_commit()

    if __name__ == "__main__":
        unittest.main()



