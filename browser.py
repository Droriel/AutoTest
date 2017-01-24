from selenium import webdriver

class Browser:
    def __init__(self):
        self.driver = None
        self.profile = None

    def start(self):
        self.driver = webdriver.Chrome('D:/Automaty/python/chromedriver.exe')
        # self.driver.get("")
        self.driver.maximize_window()
        return self.driver

    def stop(self):
        self.driver.close()