from Base.Base import Base
import Page

class Search_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_search_btn(self):
        # 点击搜索按钮
        self.click_element(Page.search_btn)
    def search_input(self, text):
        # 输入
        self.input_text(Page.search_text, text)
    def search_return(self):
        # 点击返回
        self.click_element(Page.search_return)
