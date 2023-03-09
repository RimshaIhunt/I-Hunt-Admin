import time
from selenium.webdriver import Keys

class Species:
    species_menu_xpath = "//body[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/a[1]"
    search_field_xpath = "/html/body/div[1]/div[1]/div[4]/div/div/div/div[2]/div[1]/div/input"
    species_sortingFilter_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[1]"
    addNewSpecie_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]"
    inputfield_specieName_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]"
    parentSpecie_dropdown_xpath = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]"
    specie_option_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
    choosefile_button_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/input[1]"
    submit_button_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"
    viewmodal_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/i[1]"
    viewmodal_okButton_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"
    editmodal_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[2]/i[1]"
    inputfield_editSpecies_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]"
    editSpecie_submitButton_xpath = "//body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]"
    deleteSpecie_button_xpath = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[3]/i[1]"



    def __init__(self, driver):
        self.driver = driver


    def clickOnSpecies(self):
        self.driver.find_element_by_xpath(self.species_menu_xpath).click()

    def clickOnSpeciesSearchField(self):
        click = self.driver.find_element_by_xpath(self.search_field_xpath)
        self.driver.find_element_by_xpath(self.search_field_xpath).click()
        self.driver.find_element_by_xpath(self.search_field_xpath).send_keys("coyote")
        time.sleep(2)
        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # self.driver.find_element_by_xpath(self.search_field_xpath).clear()

    def clickOnSpeciesSortingFilter(self):
        self.driver.find_element_by_xpath(self.species_sortingFilter_xpath).click()

    def clickAddNewSpeciebutton(self):
        self.driver.find_element_by_xpath(self.addNewSpecie_button_xpath).click()

    def clickOnSpecieNameField(self):
        self.driver.find_element_by_xpath(self.inputfield_specieName_xpath).send_keys("Specie")

    def clickOnParentSpecieDropdown(self):
        click = self.driver.find_element_by_xpath(self.parentSpecie_dropdown_xpath)
        click.click()

    def clickOnParentSpecieDropdownOption(self):
        specie = self.driver.find_element_by_xpath(self.specie_option_xpath)
        specie.send_keys("P")
        time.sleep(2)
        specie.send_keys(Keys.ENTER)
        time.sleep(2)

    def clickOnChooseFileButton(self):
        click = self.driver.find_element_by_xpath(self.choosefile_button_xpath)
        click.send_keys("C:\\Users\\rimsha.bashir\\Desktop\\fennac fox.jfif")

    def clickOnSubmitButton(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()

    def clickOnViewModalOfSpecies(self):
        self.driver.find_element_by_xpath(self.viewmodal_button_xpath).click()

    def clickOnViewModalOkButtonOfSpecies(self):
        self.driver.find_element_by_xpath(self.viewmodal_okButton_xpath).click()

    def clickOnEditModalOfSpecies(self):
        self.driver.find_element_by_xpath(self.editmodal_button_xpath).click()

    def EditModalOfSpecies(self):
        # self.driver.find_element_by_xpath(self.inputfield_editSiteType_xpath).clear()
        click = self.driver.find_element_by_xpath(self.inputfield_editSpecies_xpath)
        click.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        click.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.inputfield_editSpecies_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.inputfield_editSpecies_xpath).send_keys("Bear")

    def clickOnEditedSpecieSubmitbutton(self):
        self.driver.find_element_by_xpath(self.editSpecie_submitButton_xpath).click()

    def clickOnDeleteModalOfSpecies(self):
        self.driver.find_element_by_xpath(self.deleteSpecie_button_xpath).click()
