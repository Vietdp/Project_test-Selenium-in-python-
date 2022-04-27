from selenium.webdriver import Keys


class Search():
    notify = "Thông báo"
    text_search = "Tra cứu TKB"
    input_search = '//*[@id="MainContent_Ttkb1"]'
    btn_search = '//*[@id="MainContent_Lref1"]/i'


    def __init__(self, driver):
        self.driver = driver

    def clickNotify1(self):
        self.driver.find_element_by_link_text(self.notify).click()

    def clickScheduleSearch(self):
        self.driver.find_element_by_link_text(self.text_search).click()

    def setISearch(self, find):
        self.driver.find_element_by_xpath(self.input_search).send_keys(find)

    def clickBSearch(self):
        self.driver.find_element_by_xpath(self.btn_search).click()