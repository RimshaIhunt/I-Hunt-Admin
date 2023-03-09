import time
import string
import random
from pageObjects.LoginLogoutPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Users import Users

class TestCase_09_Users:
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    userfirstname = ReadConfig.userfirstname()
    userlastname = ReadConfig.userlastname()
    useremail = ReadConfig.useremail()
    useraddress = ReadConfig.useraddress()

    logger = LogGen.loggen()

    def test_Users(self, setup):
        self.logger.info("********* TestCase_Users *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        self.logger.info("********* Verified Successful Login *********")
        time.sleep(2)
        self.logger.info("********* Users *********")

        self.u = Users(self.driver)

        self.u.clickOnUsers()
        time.sleep(2)
        self.u.clickOnUsersSearchField()
        time.sleep(2)
        self.u.clickOnUsersIDSortingFilter()
        time.sleep(2)
        self.u.clickOnUsersIDSortingFilter()
        time.sleep(2)
        self.u.clickOnUsersFirstNameSortingFilter()
        time.sleep(2)
        self.u.clickOnUsersFirstNameSortingFilter()
        time.sleep(2)
        self.u.clickOnUsersLastNameSortingFilter()
        time.sleep(2)
        self.u.clickOnUsersLastNameSortingFilter()
        time.sleep(2)
        self.u.clickOnUsersEmailSortingFilter()
        time.sleep(4)
        self.u.clickOnUsersEmailSortingFilter()
        time.sleep(3)
        self.u.clickOnUsersAddNewButton()
        time.sleep(3)
        self.u.clickOnUsersAddNewFirstNameField(self.userfirstname)
        time.sleep(2)
        self.u.clickOnUsersAddNewLastNameField(self.userlastname)
        time.sleep(2)
        self.useremail = random_generator() + "@gmail.com"
        self.u.clickOnUsersAddNewEmailField(self.useremail)
        time.sleep(2)
        self.u.clickOnUsersDateOfBirthField()
        time.sleep(2)
        self.u.clickOnUsersPhoneNumberField()
        time.sleep(2)
        self.u.clickOnAddressField(self.useraddress)
        time.sleep(5)
        self.u.clickOnCityField()
        time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0, 1200);")
        self.u.clickOnStateField()
        time.sleep(2)
        self.u.clickOnStateFieldOptions()
        time.sleep(2)
        # self.u.clickOnChooseFileButton()
        # time.sleep(5)
        self.driver.save_screenshot(".//Screenshots//" + "test_Users.png")
        self.driver.close()

def random_generator(size = 8, chars = string.ascii_lowercase+string.digits):
   return ''.join(random.choice(chars) for x in range (size))