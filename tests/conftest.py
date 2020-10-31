import pytest
from selenium import webdriver


def pytest_addoption(parser):  # Registering the command line option
    parser.addoption(
        "--browser_name", action="store", default="safari", help="browsername: safari or chrome")


def pytest_report_header(config):
    """Add header to the Test NG Report"""
    return "Mobile Automation Test Report"


@pytest.fixture(scope="class")
def setup(request):  # This fixture will be called by Base class

    browser_name = request.config.getoption("--browser_name")  # Getting the Command line option
    if browser_name.upper() == 'SAFARI':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome('/Users/mandeepdhiman/Documents/Automation/Drivers/chromedriver')
    driver.get("https://www.google.ca")
    driver.maximize_window()
    request.cls.driver = driver  # assigning driver to calling class
    yield
    driver.close()  # this is teardown, ll be executed at the end of the test.


@pytest.fixture()
def load_test_data():
    print('\nI am loading test data. Before ', end='\n')
    return ['this', 'is', 'test data']
    # print('\nI am loading test data. After ', end='\n')

#
# @pytest.fixture(params=[{'browser': 'IE', "name": "INterner"}, {'browser': 'FF', "name": "Firefox"}])     # Test will be iterated through the
# def load_test_data_iterate(request):                                                #   list items
#     print('\nI am loading test data from Iteration:', end='\n')
#     print(request.param)
#     return request.param

