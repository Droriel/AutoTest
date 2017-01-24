# -*- coding: utf-8 -*-
from Pages.abstract_page import AbstractPage


class FaqPage(AbstractPage):
    locators_list = {'FAQcontent': '//*[@id="article_10154_10826_23915_1.1"]//p'}
    other_attributes_list = {'text': u'ź'}

    def __init__(self, driver):
        super().__init__(driver)
