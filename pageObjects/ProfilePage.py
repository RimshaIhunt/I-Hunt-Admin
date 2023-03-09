import time

from selenium.webdriver import Keys


class Profile:

    dropdown_profile_xpath = "/li//*[@id='navbar-main']/div/ul/a"
    dropdown_button_xpath = "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/div[1]/button[1]"
    profile_editButton_xpath = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[6]/button[2]"
    profile_submitButton_xpath = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"
    profile_backButton_xpath = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[6]/button[1]"
    inputfield_firstName_xpath = "/html/body/div[4]/div/div/div[2]/div/form/div[2]/input"
    inputfield_lastName_xpath = "/html/body/div[4]/div/div/div[2]/div/form/div[3]/input"
    countryflag_dropdown_xpath = "/html/body/div[4]/div/div/div[2]/div/form/div[5]/div[2]"
    numberfield_phone_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[5]/input[1]"
    country_dropdown_xpath = "/html/body/div[4]/div/div/div[2]/div/form/div[5]/div[2]/ul/li[143]"
    cancel_button_xpath = "/html/body/div[4]/div/div/div[2]/div/form/button[2]"
    cross_button_xpath = "/html/body/div[4]/div/div/div[1]/button/span[1]"
    usa_countryFlag_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[5]/div[2]/ul[1]/li[202]"


    def __init__(self, driver):
        self.driver = driver


    def clickOnProfileDropdown(self):
        self.driver.find_element_by_xpath(self.dropdown_profile_xpath).click()

    def clickOnProfileDropdownButton(self):
        self.driver.find_element_by_xpath(self.dropdown_button_xpath).click()

    def clickOnProfileEditButton(self):
        self.driver.find_element_by_xpath(self.profile_editButton_xpath).click()

    def setFirstName(self, firstName):
        click = self.driver.find_element_by_xpath(self.inputfield_firstName_xpath)
        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # click.clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.inputfield_firstName_xpath).send_keys("IHunt")

    def setLastName(self, lastName):
        click = self.driver.find_element_by_xpath(self.inputfield_lastName_xpath)
        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # click.clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.inputfield_lastName_xpath).send_keys("Admin")

    def clickOnCountryFlagDropdownButton(self):
        self.driver.find_element_by_xpath(self.countryflag_dropdown_xpath).click()
        self.driver.find_element_by_xpath(self.usa_countryFlag_xpath).click()

    def setPhoneNumber(self, phonenumber):
        self.driver.find_element_by_xpath(self.numberfield_phone_xpath).click()
        time.sleep(2)
        click = self.driver.find_element_by_xpath(self.numberfield_phone_xpath)
        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # click.clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.numberfield_phone_xpath).send_keys("3312345679")

    def clickOnCancelButton(self):
        self.driver.find_element_by_xpath(self.cancel_button_xpath).click()

    def clickOnCrossButton(self):
        self.driver.find_element_by_xpath(self.cross_button_xpath).click()

    def clickOnSubmitButton(self):
        self.driver.find_element_by_xpath(self.profile_submitButton_xpath).click()

    def clickOnBackButton(self):
        self.driver.find_element_by_xpath(self.profile_backButton_xpath).click()