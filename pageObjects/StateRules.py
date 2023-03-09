import time
from selenium.webdriver import Keys

class StateRules:
    staterules_menu_xpath = "//body[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/ul[1]/li[4]/a[1]"
    staterules_search_xpath = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    staterules_sortingFilter_xpath = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[1]"
    staterules_viewMode_xpath = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/a[1]/i[1]"
    staterules_okbutton_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"
    staterules_editMode_xapth = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/a[2]/i[1]"
    staterules_submitbutton_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"


    def __init__(self, driver):
        self.driver = driver

    def clickOnStateRules(self):
        self.driver.find_element_by_xpath(self.staterules_menu_xpath).click()

    def clickOnStateRulesSearchField(self):
        click = self.driver.find_element_by_xpath(self.staterules_search_xpath)
        self.driver.find_element_by_xpath(self.staterules_search_xpath).click()
        self.driver.find_element_by_xpath(self.staterules_search_xpath).send_keys("California")
        time.sleep(2)

        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)

    def clickOnStateRulesSortingFilter(self):
        self.driver.find_element_by_xpath(self.staterules_sortingFilter_xpath).click()

    def clickOnStateRulesViewMode(self):
        self.driver.find_element_by_xpath(self.staterules_viewMode_xpath).click()

    def clickOnStateRulesViewModeOkButton(self):
        self.driver.find_element_by_xpath(self.staterules_okbutton_xpath).click()

    def clickOnStateRulesEditButton(self):
        self.driver.find_element_by_xpath(self.staterules_editMode_xapth).click()

    def clickOnStateRulesEditModeSubmitButton(self):
        self.driver.find_element_by_xpath(self.staterules_submitbutton_xpath).click()

