
from gettext import find
import sys
import time


sys.path.append("C:/Users/VietDoan/Downloads/PythonFinalTest1POM")

from pageObjects.Search import Search

class TestSearch():

    find = "ST19A1B"

    def __init__(self, driver):
        self.driver = driver
        self.search = Search(driver)

    def test_func_search(self):
        self.search.clickNotify1()
        time.sleep(1)
        self.search.clickScheduleSearch()
        time.sleep(1)
        self.search.setISearch(self.find)
        time.sleep(1)
        self.search.clickBSearch()
        time.sleep(1)
        


