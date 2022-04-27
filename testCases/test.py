import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("C:/Users/VietDoan/Downloads/PythonFinalTest1POM")

from testCases.test_login_page import TestLoginPage
from testCases.test_logout_page import TestLogoutPage
from testCases.test_info_page import TestInfoPage
from testCases.test_notify_page import TestNotifyPage
from testCases.test_search import TestSearch

class MovieTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="C:\\Users\\VietDoan\\Downloads\\PythonFinalTest1POM\\drivers\\chromedriver.exe")
    baseURL = "https://my.uda.edu.vn/sv/svlogin"
    test_login_page = TestLoginPage(driver)

    test_logout_page = TestLogoutPage(driver)
    test_info_page = TestInfoPage(driver)
    test_notify_page = TestNotifyPage(driver)
    test_search = TestSearch(driver)
    
    driver.get(baseURL)
    driver.maximize_window()


    def test_page(self):
        self.test_login_page.test_func_login()
        time.sleep(2)

        self.test_notify_page.test_func_notify()
        time.sleep(2)

        self.test_search.test_func_search()
        time.sleep(2)

        self.test_info_page.test_func_info()
        time.sleep(2)

        self.test_logout_page.test_func_logout()
        time.sleep(2)
        
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))