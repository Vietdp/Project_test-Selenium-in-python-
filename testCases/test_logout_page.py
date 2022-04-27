
import sys
import time


sys.path.append("C:/Users/VietDoan/Downloads/PythonFinalTest1POM")

from pageObjects.LogoutPage import LogoutPage

class TestLogoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.logout_page = LogoutPage(driver)

    def test_func_logout(self):
        self.logout_page.clickSystem()
        time.sleep(1)
        self.logout_page.clickLogout()
        time.sleep(1)

