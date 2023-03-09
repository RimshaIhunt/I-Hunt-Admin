import time
from pageObjects.LoginLogoutPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.StateRules import StateRules
import pytest

@pytest.mark.sanity
class TestCase_08_StateRules:
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_StateRules(self, setup):
        self.logger.info("********* TestCase_StateRules *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        self.logger.info("********* Verified Successful Login *********")
        time.sleep(2)
        self.logger.info("********* State Rules *********")
        self.sr = StateRules(self.driver)

        self.sr.clickOnStateRules()
        time.sleep(2)
        self.sr.clickOnStateRulesSearchField()
        time.sleep(2)
        self.sr.clickOnStateRulesSortingFilter()
        time.sleep(2)
        self.sr.clickOnStateRulesSortingFilter()
        time.sleep(2)
        self.sr.clickOnStateRulesViewMode()
        time.sleep(2)
        self.sr.clickOnStateRulesViewModeOkButton()
        time.sleep(2)
        self.sr.clickOnStateRulesEditButton()
        time.sleep(2)
        self.sr.clickOnStateRulesEditModeSubmitButton()
        time.sleep(2)
        self.driver.save_screenshot(".//Screenshots//" + "test_State Rules.png")
        self.driver.close()