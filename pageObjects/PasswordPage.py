class Password:
    dropdown_profile_xpath = "//*[@id='navbar-main']/div/ul/li/a"
    dropdown_button_xpath = "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/div[1]/button[2]"
    inputfield_currentPassword_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]"
    inputfield_newPassword_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]"
    inputfield_confirmPassword_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/input[1]"
    changepassword_submitButton_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]"
    currentPassword_eyeIcon_xpath = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/img"
    newPassword_eyeIcon_xpath = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/img"
    confirmPassword_eyeIcon_xpath = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/img"



    def __init__(self, driver):
        self.driver = driver


    def clickOnProfileDropdown(self):
        self.driver.find_element_by_xpath(self.dropdown_profile_xpath).click()

    def clickOnProfileDropdownButton(self):
        self.driver.find_element_by_xpath(self.dropdown_button_xpath).click()

    def clickOnCurrentPasswordEyeIcon(self):
        self.driver.find_element_by_xpath(self.currentPassword_eyeIcon_xpath).click()

    def currentPassword(self):
        self.driver.find_element_by_xpath(self.inputfield_currentPassword_xpath).clear()
        self.driver.find_element_by_xpath(self.inputfield_currentPassword_xpath).send_keys("password")

    def clickOnNewPasswordEyeIcon(self):
        self.driver.find_element_by_xpath(self.newPassword_eyeIcon_xpath).click()

    def newPassword(self):
        self.driver.find_element_by_xpath(self.inputfield_newPassword_xpath).clear()
        self.driver.find_element_by_xpath(self.inputfield_newPassword_xpath).send_keys("password")

    def clickOnConfirmPasswordEyeIcon(self):
        self.driver.find_element_by_xpath(self.confirmPassword_eyeIcon_xpath).click()

    def confirmPassword(self):
        self.driver.find_element_by_xpath(self.inputfield_confirmPassword_xpath).clear()
        self.driver.find_element_by_xpath(self.inputfield_confirmPassword_xpath).send_keys("password")

    def clickOnSubmitButton(self):
        self.driver.find_element_by_xpath(self.changepassword_submitButton_xpath).click()