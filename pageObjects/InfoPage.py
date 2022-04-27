from selenium.webdriver import Keys

class InfoPage():
    text_private_corner = "Góc sinh viên"
    text_info = "Thông tin cá nhân"



    def __init__(self, driver):
        self.driver = driver


    def clickPrivate(self):
        self.driver.find_element_by_link_text(self.text_private_corner).click()

    def clickInfo(self):
        self.driver.find_element_by_link_text(self.text_info).click()