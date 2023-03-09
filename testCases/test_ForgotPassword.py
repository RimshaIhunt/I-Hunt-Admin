import time
from pageObjects.ForgotPasswordPage import ForgotPassword
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestCase_04_ForgotPassword:
    baseURL = ReadConfig.getURL()
    logger = LogGen.loggen()

    def test_forgotPassword(self, setup):
        self.logger.info("********* TestCase_04_ForgotPassword *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.fp = ForgotPassword(self.driver)
        self.fp.clickOnForgotPasswordButton()
        self.fp.enteringEmail()
        self.fp.clickOnVerifyEmailButton()
        self.logger.info("********* Verification link sent to the provided link *********")
        time.sleep(3)
        self.driver.save_screenshot(".//Screenshots//" + "test_ForgotPassword.png")
        self.fp.clickOnForgotPasswordButton()
        time.sleep(5)
        self.fp.clickOnBackButton()
        self.driver.save_screenshot(".//Screenshots//" + "test_profile.png")
        self.driver.close()
