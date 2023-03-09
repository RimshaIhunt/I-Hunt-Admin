class Login:
    inputfield_email_xpath = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]"
    inputfield_password_xpath = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]"
    button_login_xpath = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]"
    dropdown_profile_xpath = "//body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/span[1]"
    logout_button_xpath = "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/div[1]/button[3]"
    modal_button_xpath = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[3]/button[2]"

    def __init__(self, driver):
        self.driver = driver


    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.inputfield_email_xpath).clear()
        self.driver.find_element_by_xpath(self.inputfield_email_xpath).send_keys("salman.ihunt+2533@nxvt.com")

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.inputfield_password_xpath).clear()
        self.driver.find_element_by_xpath(self.inputfield_password_xpath).send_keys("password")

    def loginButton(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickOnProfileDropdown(self):
         self.driver.find_element_by_xpath(self.dropdown_profile_xpath).click()

    def clickOnProfileDropdownButton(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

    def clickOnModalButton(self):
        self.driver.find_element_by_xpath(self.modal_button_xpath).click()