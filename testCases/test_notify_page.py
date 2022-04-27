
import sys
import time


sys.path.append("C:/Users/VietDoan/Downloads/PythonFinalTest1POM")

from pageObjects.Notify import NotifyPage

class TestNotifyPage():

    def __init__(self, driver):
        self.driver = driver
        self.notify_page = NotifyPage(driver)

    def test_func_notify(self):
        self.notify_page.clickNotify()
        time.sleep(1)
        self.notify_page.clickSchedule()
        time.sleep(1)

