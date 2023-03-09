import time
from pageObjects.LoginLogoutPage import Login
from pageObjects.PasswordPage import Password
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

class TestCase_03_Password:
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_Password(self, setup):
        self.logger.info("********* TestCase_03_ChangePassword *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        self.logger.info("********* Verified Successful Login *********")
        time.sleep(3)
        self.logger.info("********* ChangePassword *********")

        self.cp = Password(self.driver)

        self.cp.clickOnProfileDropdown()
        self.cp.clickOnProfileDropdownButton()
        time.sleep(2)
        self.cp.clickOnCurrentPasswordEyeIcon()
        time.sleep(2)
        self.cp.currentPassword()
        self.cp.clickOnNewPasswordEyeIcon()
        time.sleep(2)
        self.cp.newPassword()
        self.cp.clickOnConfirmPasswordEyeIcon()
        time.sleep(2)
        self.cp.confirmPassword()
        self.cp.clickOnSubmitButton()
        time.sleep(3)
        self.driver.save_screenshot(".//Screenshots//" + "test_ChangePassword.png")
        self.driver.close()



