"""Temp information"""


class SessionAssistant:

    def __init__(self, conf):
        self.conf = conf

    def login(self, email: str, password: str):
        driver = self.conf.driver
        self.conf.open_login_page()
        self.inputted_data("input-email", email)
        self.inputted_data("input-password", password)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

    def inputted_data(self, field: str, data: str):
        driver = self.conf.driver
        driver.find_element_by_id(field).click()
        driver.find_element_by_id(field).clear()
        driver.find_element_by_id(field).send_keys(data)

    def logout(self):
        driver = self.conf.driver
        driver.find_element_by_xpath("//ul[@class='list-inline']//a[.=' My Account ']").click()
        driver.find_element_by_xpath("//ul[@class='list-inline']//a[.='Logout']").click()
