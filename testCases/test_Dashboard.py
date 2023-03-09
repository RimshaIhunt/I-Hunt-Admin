import time
from pageObjects.LoginLogoutPage import Login
from pageObjects.DashboardPage import Dashboard
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

@pytest.mark.sanity
class TestCase_05_Dashboard:
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_dashboard(self, setup):
        self.logger.info("********* TestCase_05_DashBoard *********")
        self.logger.info("********* Verified Successfull Login *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        time.sleep(3)
        self.db = Dashboard(self.driver)
        time.sleep(2)
        self.db.clickOnApproveStandsCard()
        time.sleep(2)
        self.db.clickOnDashboardButton()
        time.sleep(2)
        self.db.clickOnPendingStandsCard()
        time.sleep(2)
        self.db.clickOnDashboardButton()
        # time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0, 1650);")
        # time.sleep(2)
        # self.db.clickOnStandTrophiesfromSearchButton()
        # time.sleep(2)
        # self.db.clickOnStandTrophiestoSearchButton()
        # time.sleep(2)
        # self.db.clickOnTrophiesSearchButton()
        # time.sleep(2)
        # self.db.clickOnTrophiesDownloadButton()
        # time.sleep(2)
        # self.db.clickOnTrophiesViewButton()
        # time.sleep(3)
        # self.db.clickOnDashboardButton()
        # time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0, 1650);")
        # time.sleep(2)
        # self.db.clickOnRentedStandsfromSearchButton()
        # time.sleep(2)
        # self.db.clickOnRentedStandtoSearchButton()
        # time.sleep(2)
        # self.db.clickOnRentedSearchButton()
        # time.sleep(2)
        # self.db.clickOnRentedDownloadButton()
        # time.sleep(2)
        # self.db.clickOnRentedViewButton()
        # time.sleep(2)
        # self.db.clickOnDashboardButton()
        # time.sleep(2)
        self.driver.save_screenshot(".//Screenshots//" + "test_Dashboard.png")
        self.driver.close()
