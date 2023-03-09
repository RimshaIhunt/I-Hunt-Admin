import time
from pageObjects.LoginLogoutPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

@pytest.mark.sanity
# @pytest.mark.regression
class TestCase_01_Login:
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("********* TestCase_01_Login *********")
        self.logger.info("********* Verified Successful Login *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        time.sleep(5)
        # self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
        # self.lp.clickOnProfileDropdown()
        # time.sleep(5)
        # self.lp.clickOnProfileDropdownButton()
        # time.sleep(3)
        # self.driver.save_screenshot(".//Screenshots//"+"test_logout.png")
        # self.lp.clickOnModalButton()
        # self.driver.close()
