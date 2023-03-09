import time
from selenium.webdriver import Keys

class Types:
    siteTypes_menu_xpath = "//body[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]"
    search_field_xpath = "/html/body/div[1]/div[1]/div[4]/div/div/div/div[2]/div[1]/div/input"
    siteTypes_sortingFilter_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[1]"
    addNewSiteType_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]"
    inputfield_siteType_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]"
    siteType_submitButton_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"
    viewmodal_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/i[1]"
    viewmodal_okButton_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"
    editmodal_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[2]/i[1]"
    inputfield_editSiteType_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]"
    editSiteType_submitButton_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"
    deleteSiteType_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[3]/i[1]"
    delete_button_xpath = "//body[1]/div[4]/div[1]/div[1]/div[3]/div[1]/button[2]"


    def __init__(self, driver):
        self.driver = driver


    def clickOnSiteTypes(self):
        self.driver.find_element_by_xpath(self.siteTypes_menu_xpath).click()

    def clickOnSiteTypesSearchField(self):
        click = self.driver.find_element_by_xpath(self.search_field_xpath)
        self.driver.find_element_by_xpath(self.search_field_xpath).click()
        self.driver.find_element_by_xpath(self.search_field_xpath).send_keys("Norway")
        time.sleep(2)

        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # self.driver.find_element_by_xpath(self.search_field_xpath).clear()

    def clickOnSiteTypesSortingFilter(self):
        self.driver.find_element_by_xpath(self.siteTypes_sortingFilter_xpath).click()

    def clickAddNewSiteTypesbutton(self):
        self.driver.find_element_by_xpath(self.addNewSiteType_button_xpath).click()

    def addNewSiteType(self):
        self.driver.find_element_by_xpath(self.inputfield_siteType_xpath).send_keys("Norway")

    def clickSiteTypeSubmitbutton(self):
        self.driver.find_element_by_xpath(self.siteType_submitButton_xpath).click()

    def clickOnViewModalOfSiteType(self):
        self.driver.find_element_by_xpath(self.viewmodal_button_xpath).click()

    def clickOnViewModalOkButtonSiteTypeSubmit(self):
        self.driver.find_element_by_xpath(self.viewmodal_okButton_xpath).click()

    def clickOnEditModalOfSiteType(self):
        self.driver.find_element_by_xpath(self.editmodal_button_xpath).click()

    def EditModalOfSiteTypes(self):
        # self.driver.find_element_by_xpath(self.inputfield_editSiteType_xpath).clear()
        click = self.driver.find_element_by_xpath(self.inputfield_editSiteType_xpath)
        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.inputfield_editSiteType_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.inputfield_siteType_xpath).send_keys("Kategat")

    def clickOnEditedSiteTypeSubmitbutton(self):
        self.driver.find_element_by_xpath(self.editSiteType_submitButton_xpath).click()

    def clickOnDeleteModalOfSiteTypes(self):
        self.driver.find_element_by_xpath(self.deleteSiteType_button_xpath).click()

    def clickOnDeleteButton(self):
        self.driver.find_element_by_xpath(self.delete_button_xpath)
