class ForgotPassword:
    forgotPassword_button_xpath = '/html/body/div[1]/div[1]/div[2]/div/div/div/div/form/a/small'
    inputfield_email_xpath = '/html/body/div[1]/div[1]/div[2]/div/div/div/div/form/div[1]/input'
    verifyEmail_button_xpath = '/html/body/div[1]/div[1]/div[2]/div/div/div/div/form/div[2]/button[2]'
    back_button_xpath = '/html/body/div[1]/div[1]/div[2]/div/div/div/div/form/div[2]/button[1]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnForgotPasswordButton(self):
        self.driver.find_element_by_xpath(self.forgotPassword_button_xpath).click()

    def enteringEmail(self):
        self.driver.find_element_by_xpath(self.inputfield_email_xpath).clear()
        self.driver.find_element_by_xpath(self.inputfield_email_xpath).send_keys("rimsha.bashir@nxb.com.pk")

    def clickOnVerifyEmailButton(self):
        self.driver.find_element_by_xpath(self.verifyEmail_button_xpath).click()

    def clickOnBackButton(self):
        self.driver.find_element_by_xpath(self.back_button_xpath).click()