import pytest
from utilities.readProperties import ReadConfig
from testCases.test_LoginLogout import TestCase_01_Login
from testCases.test_Profile import TestCase_02_Profile
from testCases.test_Password import TestCase_03_Password
from testCases.test_ForgotPassword import TestCase_04_ForgotPassword
from testCases.test_Dashboard import TestCase_05_Dashboard
from testCases.test_HuntingSiteTypes import TestCase_06_SiteTypes
from testCases.test_Species import TestCase_07_Species
from testCases.test_StateRules import TestCase_08_StateRules


@pytest.mark.incremental

class TestSequential:

    baseURL = ReadConfig.getURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    def test_first(self):

        self.tc1 = TestCase_01_Login
        print('first test case')

    def test_second(self):

        self.tc2 = TestCase_02_Profile
        print('second test case')

    def test_third(self):

        self.tc3 = TestCase_03_Password
        print('third test case')

    def test_fourth(self):

        self.tc4 = TestCase_04_ForgotPassword
        print('fourth test case')

    def test_fifth(self):

        self.tc5 = TestCase_05_Dashboard
        print('fifth test case')

    def test_sixth(self):

        self.tc6 = TestCase_06_SiteTypes
        print('sixth test case')

    def test_seventh(self):

        self.tc7 = TestCase_07_Species
        print('seventh test case')

    def test_eighth(self):

        self.tc7 = TestCase_08_StateRules
        print('eighth test case')
