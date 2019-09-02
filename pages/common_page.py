
from pages.base_page import BasePage
from pages.page_object import FindElement, FindElements


class CommonPage(BasePage):
    welcome_title = FindElement(id_="welcome_title")
    welcome_button = FindElement(id_="welcome_button")

    # 跳过欢迎页
    def skip_welcome_page(self):
        if self.welcome_title:
            self.swipe_left(count=2)
            self.welcome_button.click()


