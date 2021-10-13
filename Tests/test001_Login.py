import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.iniReader import ReadIni

@pytest.mark.usefixtures('setup')
class Test_001_login:
    baseURL = ReadIni.getApplicationURL()
    username = ReadIni.getUsername()
    password = ReadIni.getPassword()

    def test_login(self, setup):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoinBtn()

        assert self.driver.title == "OrangeHRM"
