# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AbstractPage(object):
        main_page_list = {'main_page': 'http://pg.edu.pl/', 'dzial_archiwum': 'dzial-obiegu-i-archiwizacji-dokumentow/'}

        def __init__(self, driver):
            self.driver = driver

        def take_url(self):
            return self.driver.current_url

        # def check_is_there_text(self):
        def find_href(self, lokator):
            try:
                self.driver.find_element_by_css_selector(lokator)
                return True
            except:
                return False

        def find_visible_href(self, lokator):
            try:
                href = self.driver.find_element_by_css_selector(lokator)
                if href.is_displayed():
                    return True
                else:
                    return False
            except:
                return False

        def wait_for_text_in_element(self,elIdXPath,text):
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, elIdXPath)))
            try:
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.text_to_be_present_in_element((By.XPATH, elIdXPath), text))
            except:
                print('Brak tekstu %s w elemencie %s' % (text, elIdXPath))
