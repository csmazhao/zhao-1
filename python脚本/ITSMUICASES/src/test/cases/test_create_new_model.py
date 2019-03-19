#coding=utf-8
import  unittest
import time
class createnewmodel(unittest.TestCase):

    def test_createnewmodel(self):
        admin =self.src.test.common.login(name=self.src.test.common.globals.glv.gl_admin,pasword=self.src.test.common.globals.glv.gl_adminpas)
        self.driver =self.src.test.common.login.userlogin(admin)
        model =self.src.test.pages.newmodel(self.driver)
        menu = self.src.test.pages.leftmenu(self.driver)
        menu.link_model_mange()
        manage = self.src.test.pages.modelManage(self.driver)
        manage.new_model_btn()
        #创建事件工单类型模型
        manage.model_type_switch("事件工单")
        model.set_newmodel_name()
        model.set_newmodel_prefix()
        model.set_newmodel_gdgzdate(self.src.test.common.globals.glv.gl_mode_longdate)
        model.set_newmodel_gdgz_flowno(self.src.test.common.globals.glv.gl_model_flowno_five)
        #添加管理员
        model.set_newmodel_admin(self.src.test.common.globals.glv.gl_admin)
        #授权用户
        model.set_admin_auth()
        #保存
        time.sleep(2)
        model.save_model_configuration()
        manage.switch_model_using(self.src.test.common.globals.glv.gl_model_name)
        result =  manage.is_model_exist(self.src.test.common.globals.glv.gl_model_name)
        self.assertTrue(result,"model is not exist, create model failed.")

    def tearDown(self):
        pass
    if __name__ == '__main__':
        unittest.main()


