from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element_o(self,loc, timeout=10, poll=0.5):
        """
        :param loc: 元祖(By.ID,ID属性值)
        :param timeout:
        :param poll:
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        # 点击函数
        self.find_element_o(loc).click()
    def input_text(self, loc, text):
        """
        :param loc:
        :param text: 输入的内容
        :return:
        """
        ele = self.find_element_o(loc)
        ele.clear()
        ele.send_keys(text)

