from Base.Base import Base
import Page, time

class Add_User_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_add(self):
        # 点击添加用户按钮
        print("Page.add_user:",Page.add_user)
        self.click_element(Page.add_user)

    def click_save_local(self):
        # 点击本地保存
        self.click_element(Page.save_local)

    def input_user_info(self, name, phone):
        # 输入用户名
        self.input_text(Page.send_name, name)
        # 电话 点击返回保存
        self.input_text(Page.send_phone, phone)
        # 点击返回保存
        self.click_element(Page.click_save_back)
        time.sleep(5)
        self.driver.keyevent(4)