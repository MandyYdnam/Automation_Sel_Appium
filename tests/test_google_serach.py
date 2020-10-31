from pageObjects.search_page import SearchPage
from utilities.BaseClass import BaseClass
from testData.TestData import TestDataFactory
from selenium import webdriver
import pytest


class TestGoogle(BaseClass):
    # driver = webdriver.Chrome()

    def test_search(self, get_data):
        # self.driver.find_element_by_name('q').send_keys('this is just  a test')
        logger = self.get_logger()
        self.wait_until_element_is_visible(SearchPage(self.driver).get_search_box())
        logger.info('Entering Serach String:%s', get_data['name'])
        print('Entering Serach String:{}', get_data['name'])
        SearchPage(self.driver).get_search_box().send_keys(get_data['name'])
        self.driver.save_screenshot('test.jpg')
        logger = None

    def test_search2(self, get_data):
        # self.driver.find_element_by_name('q').send_keys('this is just  a test')
        logger = self.get_logger()
        self.wait_until_element_is_visible(SearchPage(self.driver).get_search_box())
        logger.info('Entering Serach String:%s', get_data['name'])
        SearchPage(self.driver).get_search_box().send_keys(get_data['name'])
        self.driver.save_screenshot('test.jpg')

    @pytest.fixture(params=TestDataFactory.test_google_search_test_google)
    def get_data(self, request):
        return request.param
