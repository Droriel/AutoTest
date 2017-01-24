# -*- coding: utf-8 -*-
from Pages.abstract_page import AbstractPage
from Pages.faq_page import FaqPage


class OpenPage(AbstractPage):
    def __init__(self, driver):
        # na init stanąć i alt+enter stworzy superklasę
        super().__init__(driver)
#       py 2.7  super(OpenPage, self).__init__(driver)

    def open_simple_pages(self):
        self.driver.get(self.main_page_list['main_page'] + self.main_page_list['dzial_archiwum'])

    def open_page_faq(self):
        self.driver.find_element_by_id("n1").click()
        return FaqPage(self.driver)
