from selenium.webdriver import Keys

class LogoutPage():
    text_system_id = "Hệ thống"
    text_logout_id = "Đăng xuất"



    def __init__(self, driver):
        self.driver = driver


    def clickSystem(self):
        self.driver.find_element_by_link_text(self.text_system_id).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.text_logout_id).click()