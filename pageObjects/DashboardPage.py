class Dashboard:
    approveStand_card_xpath = '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div'
    dashboard_button_xpath = '//body[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]'
    pendingStands_card_xpath = '/html/body/div[1]/div[1]/div[3]/div[1]/div[3]/div'
    # standtrophies_fromsearch_xpath = '/html/body/div[1]/div[1]/div[3]/div[4]/div[1]/div/div/div/div/form/div[1]/div[1]/input'
    # standstrophies_tosearch_xpath = '/html[1]/body[1]/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]'
    # trophiessearch_button_xpath = '/html/body/div[1]/div[1]/div[3]/div[4]/div[1]/div/div/div/div/form/div[2]/button[1]'
    # tophiesdownload_button_xpath = '/html/body/div[1]/div[1]/div[3]/div[4]/div[1]/div/div/div/div/form/div[2]/button[3]'
    # trophiesView_button_xpath = '/html/body/div[1]/div[1]/div[3]/div[4]/div[1]/div/div/div/div/form/div[2]/button[2]'
    # rentedStands_fromsearch_xpath = '/html/body/div[1]/div[1]/div[3]/div[4]/div[2]/div/div/div/div/form/div[1]/div[1]/input'
    # rentedStands_tosearch_xpath = '/html[1]/body[1]/div[1]/div[1]/div[3]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]'
    # rentedsearch_button_xpath = '/html/body/div[1]/div[1]/div[3]/div[4]/div[2]/div/div/div/div/form/div[2]/button'
    # rentedDownload_button_xapth = '/html/body/div[1]/div[1]/div[3]/div[4]/div[2]/div/div/div/div/form/div[2]/button[3]'
    # rentedView_button_xpath = '/html/body/div[1]/div[1]/div[3]/div[4]/div[2]/div/div/div/div/form/div[2]/button[2]'


    def __init__(self, driver):
        self.driver = driver

    def clickOnApproveStandsCard(self):
        self.driver.find_element_by_xpath(self.approveStand_card_xpath).click()

    def clickOnDashboardButton(self):
        self.driver.find_element_by_xpath(self.dashboard_button_xpath).click()

    def clickOnPendingStandsCard(self):
        self.driver.find_element_by_xpath(self.pendingStands_card_xpath).click()

    # def clickOnStandTrophiesfromSearchButton(self):
    #     self.driver.find_element_by_xpath(self.standtrophies_fromsearch_xpath).send_keys("02022022")
    #
    # def clickOnStandTrophiestoSearchButton(self):
    #     self.driver.find_element_by_xpath(self.standstrophies_tosearch_xpath).send_keys("09082022")
    #
    # def clickOnTrophiesSearchButton(self):
    #     self.driver.find_element_by_xpath(self.trophiessearch_button_xpath).click()
    #
    # def clickOnTrophiesDownloadButton(self):
    #     self.driver.find_element_by_xpath(self.tophiesdownload_button_xpath).click()
    #
    # def clickOnTrophiesViewButton(self):
    #     self.driver.find_element_by_xpath(self.trophiesView_button_xpath).click()
    #
    # def clickOnRentedStandsfromSearchButton(self):
    #     self.driver.find_element_by_xpath(self.rentedStands_fromsearch_xpath).send_keys("02022022")
    #
    # def clickOnRentedStandtoSearchButton(self):
    #     self.driver.find_element_by_xpath(self.rentedStands_tosearch_xpath).send_keys("09082022")
    #
    # def clickOnRentedSearchButton(self):
    #     self.driver.find_element_by_xpath(self.rentedsearch_button_xpath).click()
    #
    # def clickOnRentedDownloadButton(self):
    #     self.driver.find_element_by_xpath(self.rentedDownload_button_xapth).click()
    #
    # def clickOnRentedViewButton(self):
    #     self.driver.find_element_by_xpath(self.rentedView_button_xpath).click()