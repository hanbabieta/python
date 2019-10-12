from Page.add_user_page import Add_User_Page
from Page.search_page import Search_Page

class Page_Obj:
    def __init__(self, driver):
        self.driver = driver

    def return_add_user(self):
        # 添加用户
        return Add_User_Page(self.driver)
    def return_search(self):
        # 搜游页面对象
        return Search_Page(self.driver)