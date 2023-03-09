import random
import string
import time
from selenium.webdriver import Keys

class Users:
    users_menu_xpath = "//body[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/ul[1]/li[5]/a[1]"
    users_search_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    users_idsorting_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[1]"
    users_firstNameSorting_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[2]"
    users_lastNameSorting_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[3]"
    users_emailSorting_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[4]"
    addNewUser_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]"
    choosefile_button_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/label[1]/i[1]"
    firstname_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]"
    lastname_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/input[1]"
    email_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/input[1]"
    dob_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/input[1]"
    date_button_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]"
    phonenumber_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/input[1]"
    address_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[5]/div[1]/div[1]/input[1]"
    city_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[5]/div[2]/div[1]/input[1]"
    state_dropdown_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]"
    statedropdown_option_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]"
    country_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[6]/div[2]/div[1]/input[1]"
    zip_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[6]/div[2]/div[1]/input[1]"
    password_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[8]/div[1]/div[1]/input[1]"
    password_eyeicon_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[8]/div[1]/div[1]/img[1]"
    confirmpassword_field_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[8]/div[1]/div[1]/input[1]"
    confirmpassword_eyeicon_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[8]/div[2]/div[1]/img[1]"



    def __init__(self, driver):
        self.driver = driver

    def clickOnUsers(self):
        self.driver.find_element_by_xpath(self.users_menu_xpath).click()

    def clickOnUsersSearchField(self):
        click = self.driver.find_element_by_xpath(self.users_search_xpath)
        self.driver.find_element_by_xpath(self.users_search_xpath).click()
        self.driver.find_element_by_xpath(self.users_search_xpath).send_keys("Rimsha")
        time.sleep(2)
        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)

    def clickOnUsersIDSortingFilter(self):
        self.driver.find_element_by_xpath(self.users_idsorting_xpath).click()

    def clickOnUsersFirstNameSortingFilter(self):
        self.driver.find_element_by_xpath(self.users_firstNameSorting_xpath).click()

    def clickOnUsersLastNameSortingFilter(self):
        self.driver.find_element_by_xpath(self.users_lastNameSorting_xpath).click()

    def clickOnUsersEmailSortingFilter(self):
        self.driver.find_element_by_xpath(self.users_emailSorting_xpath).click()

    def clickOnUsersAddNewButton(self):
        self.driver.find_element_by_xpath(self.addNewUser_button_xpath).click()

    def clickOnUsersAddNewFirstNameField(self, firstname):
        self.driver.find_element_by_xpath(self.firstname_field_xpath).click()
        self.driver.find_element_by_xpath(self.firstname_field_xpath).send_keys("Rimsha")

    def clickOnUsersAddNewLastNameField(self, lastname):
        self.driver.find_element_by_xpath(self.lastname_field_xpath).click()
        self.driver.find_element_by_xpath(self.lastname_field_xpath).send_keys("Bashir")

    def clickOnUsersAddNewEmailField(self, email):
        self.driver.find_element_by_xpath(self.email_field_xpath).send_keys(email)

    def clickOnUsersDateOfBirthField(self):
        self.driver.find_element_by_xpath(self.dob_field_xpath).click()
        self.driver.find_element_by_xpath(self.date_button_xpath).click()

    def clickOnUsersPhoneNumberField(self):
        self.driver.find_element_by_xpath(self.phonenumber_field_xpath).click()
        self.driver.find_element_by_xpath(self.phonenumber_field_xpath).send_keys("2311234432")

    def clickOnAddressField(self, address):
        self.driver.find_element_by_xpath(self.address_field_xpath).click()
        self.driver.find_element_by_xpath(self.address_field_xpath).send_keys("Miami, FL, USA")

    def clickOnCityField(self):
        self.driver.find_element_by_xpath(self.city_field_xpath).click()
        self.driver.find_element_by_xpath(self.city_field_xpath).send_keys("Miami")

    def clickOnStateField(self):
        state = self.driver.find_element_by_xpath(self.state_dropdown_xpath)
        state.click()

    def clickOnStateFieldOptions(self):
        option = self.driver.find_element_by_xpath(self.statedropdown_option_xpath)
        option.send_keys("Fl")
        time.sleep(5)
        # state.click()
        # time.sleep(5)
        # state.send_keys(Keys.ARROW_DOWN)
        # time.sleep(5)

        option.send_keys(Keys.ENTER)
        time.sleep(2)



    # def clickOnChooseFileButton(self):
    #     click = self.driver.find_element_by_xpath(self.choosefile_button_xpath).click()
    #     # click.click()
    #     click.send_keys("C:\\Users\\rimsha.bashir\\Desktop\\head explosion.jpg")



