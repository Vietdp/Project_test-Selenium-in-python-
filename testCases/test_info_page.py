
import sys
import time


sys.path.append("C:/Users/VietDoan/Downloads/PythonFinalTest1POM")

from pageObjects.InfoPage import InfoPage

class TestInfoPage():

    def __init__(self, driver):
        self.driver = driver
        self.info_page = InfoPage(driver)

    def test_func_info(self):
        self.info_page.clickPrivate()
        time.sleep(1)
        self.info_page.clickInfo()
        time.sleep(1)

