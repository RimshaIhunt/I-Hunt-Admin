import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser..........")
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser..........")
        driver.maximize_window()
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# def pytest_configure(config):
#     config.metadata['Project Name'] = 'I-Hunt'
#     config.metadata['Module Name'] = 'Login'
#     config.metadata['Tester'] = 'Rimsha Bashir'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Java_Home", None)
#     metadata.pop("Plugins", None)

