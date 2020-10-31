from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome()


class SearchPage:
    search_box = (By.NAME, 'q')

    def __init__(self, driver):
        self.driver = driver

    def get_search_box(self):
        return self.driver.find_element(*SearchPage.search_box)