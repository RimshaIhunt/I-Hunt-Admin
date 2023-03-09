import time
from pageObjects.LoginLogoutPage import Login
from pageObjects.ProfilePage import Profile
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestCase_02_Profile:
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    firsName = ReadConfig.firstName()
    lastName = ReadConfig.lastName()
    phoneNumber = ReadConfig.phonenumber()

    logger = LogGen.loggen()

    def test_Profile(self, setup):
        self.logger.info("********* TestCase_02_Profile *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        self.logger.info("********* Verified Successful Login *********")
        time.sleep(5)
        self.logger.info("********* Profile *********")

        self.p = Profile(self.driver)

        self.p.clickOnProfileDropdown()
        self.p.clickOnProfileDropdownButton()
        time.sleep(2)
        self.p.clickOnProfileEditButton()
        time.sleep(2)
        self.p.clickOnCancelButton()
        time.sleep(2)
        self.p.clickOnProfileEditButton()
        time.sleep(2)
        self.p.clickOnCrossButton()
        time.sleep(2)
        self.p.clickOnProfileEditButton()
        time.sleep(2)
        self.p.setFirstName(self.firsName)
        time.sleep(2)
        self.p.setLastName(self.lastName)
        time.sleep(2)
        self.p.clickOnCountryFlagDropdownButton()
        time.sleep(2)
        self.p.setPhoneNumber(self.phoneNumber)
        time.sleep(2)
        self.p.clickOnSubmitButton()
        time.sleep(3)
        self.p.clickOnBackButton()
        time.sleep(3)
        self.driver.save_screenshot(".//Screenshots//" + "test_profile.png")
        self.driver.close()


