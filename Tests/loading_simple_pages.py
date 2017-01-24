# -*- coding: utf-8 -*-

#alt+enter na klasie z innego pliku żeby ją zaimportować
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.open_page import OpenPage
from browser import Browser

#W każdym pliku testu jedna główna klasa - musi mieć nazwę kończącą się na Test - potem tak zaczynają się z kolei nazwy metod

class LoadingSimplePagesTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_simple_pages()

    def test_open_page_FAQ(self):
        page_faq = OpenPage(self.driver).open_page_faq()
        self.assertEqual(page_faq.take_url(), 'http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/faq', 'FAQ - Błędny adres URL')
        self.assertTrue(page_faq.find_visible_href('[href="http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/faq"]'), 'Brak widocznego linka FAQ')
        # zawsze self.driver + czas
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,'article_10154_10826_23915_1.1')))
        # WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, elId)))
        page_faq.wait_for_text_in_element(page_faq.locators_list['FAQcontent'], page_faq.other_attributes_list['text'])
