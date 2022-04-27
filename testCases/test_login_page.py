
import sys
import time


sys.path.append("C:/Users/VietDoan/Downloads/PythonFinalTest1POM")

from pageObjects.LoginPage import LoginPage

class TestLoginPage():

    username = "48597"
    password = "0983991247"

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def test_func_login(self):
        self.login_page.setUserName(self.username)
        time.sleep(1)
        self.login_page.setPassword(self.password)
        time.sleep(1)
        self.login_page.clickLogin()
        time.sleep(1)
        


