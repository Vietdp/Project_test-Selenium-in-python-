from selenium.webdriver import Keys

class NotifyPage():
    text_notify = "Thông báo"
    text_schedule = "Thời khóa biểu"



    def __init__(self, driver):
        self.driver = driver


    def clickNotify(self):
        self.driver.find_element_by_link_text(self.text_notify).click()

    def clickSchedule(self):
        self.driver.find_element_by_link_text(self.text_schedule).click()