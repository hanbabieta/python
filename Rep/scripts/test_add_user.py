import sys, os

sys.path.append(os.getcwd()) # /Users/li/Documents/Worker/Rep

from Base.InitDiver import init_driver
from Page.Page import Page_Obj
import pytest

class Test_Add_User:
    def setup_class(self):
        self.driver = init_driver()
        self.add_user_obj = Page_Obj(self.driver).return_add_user()

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture()
    def add_user_btn(self):
        # 添加用户
        self.add_user_obj.click_add()

    @pytest.fixture(scope="class")
    def save_local_btn(self):
        # 点击本地保存
        self.add_user_obj.click_save_local()

    @pytest.mark.usefixtures("add_user_btn", "save_local_btn")
    @pytest.mark.parametrize("name, phone",[("李001","13333333333"),("李002","13555555555")])
    def test_input_user_info(self, name, phone):
        self.add_user_obj.input_user_info(name, phone)