import time
from pageObjects.LoginLogoutPage import Login
from pageObjects.HuntingSiteTypes import Types
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

@pytest.mark.sanity
class TestCase_06_SiteTypes:
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_SiteTypes(self, setup):
        self.logger.info("********* TestCase_SiteTypes *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        self.logger.info("********* Verified Successful Login *********")
        time.sleep(5)
        self.logger.info("********* SiteTypes *********")

        self.st = Types(self.driver)
        self.st.clickOnSiteTypes()
        time.sleep(2)
        self.st.clickOnSiteTypesSearchField()
        time.sleep(2)
        self.st.clickOnSiteTypesSortingFilter()
        time.sleep(2)
        self.st.clickOnSiteTypesSortingFilter()
        time.sleep(2)
        self.st.clickAddNewSiteTypesbutton()
        time.sleep(2)
        self.st.addNewSiteType()
        time.sleep(2)
        self.st.clickSiteTypeSubmitbutton()
        time.sleep(2)
        self.st.clickOnViewModalOfSiteType()
        time.sleep(2)
        self.st.clickOnViewModalOkButtonSiteTypeSubmit()
        time.sleep(2)
        self.st.clickOnEditModalOfSiteType()
        time.sleep(2)
        self.st.EditModalOfSiteTypes()
        time.sleep(2)
        self.st.clickOnEditedSiteTypeSubmitbutton()
        time.sleep(2)
        self.st.clickOnDeleteModalOfSiteTypes()
        time.sleep(2)
        self.st.clickOnDeleteButton()
        time.sleep(2)
        self.driver.save_screenshot(".//Screenshots//" + "test_Site Types.png")
        self.driver.close()