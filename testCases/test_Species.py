import time
from pageObjects.LoginLogoutPage import Login
from pageObjects.Species import Species
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

@pytest.mark.sanity
class TestCase_07_Species:
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_Species(self, setup):
        self.logger.info("********* TestCase_species *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        self.logger.info("********* Verified Successful Login *********")
        self.logger.info("********* Species *********")

        self.s = Species(self.driver)
        time.sleep(2)
        self.s.clickOnSpecies()
        time.sleep(2)
        self.s.clickOnSpeciesSearchField()
        time.sleep(2)
        self.s.clickOnSpeciesSortingFilter()
        time.sleep(2)
        self.s.clickOnSpeciesSortingFilter()
        time.sleep(2)
        self.s.clickAddNewSpeciebutton()
        time.sleep(2)
        self.s.clickOnSpecieNameField()
        time.sleep(2)
        self.s.clickOnParentSpecieDropdown()
        time.sleep(2)
        self.s.clickOnParentSpecieDropdownOption()
        time.sleep(2)
        self.s.clickOnChooseFileButton()
        time.sleep(2)
        self.s.clickOnSubmitButton()
        time.sleep(2)
        self.s.clickOnViewModalOfSpecies()
        time.sleep(2)
        self.s.clickOnViewModalOkButtonOfSpecies()
        time.sleep(2)
        self.s.clickOnEditModalOfSpecies()
        time.sleep(2)
        self.s.EditModalOfSpecies()
        time.sleep(2)
        self.s.clickOnEditedSpecieSubmitbutton()
        time.sleep(2)
        self.s.clickOnDeleteModalOfSpecies()
        time.sleep(2)
        self.driver.save_screenshot(".//Screenshots//" + "test_Species.png")
        self.driver.close()