"""Temp info."""


class UserDetailsAssistant:

    def __init__(self, conf):
        self.conf = conf

    def open_user_edit_form(self):
        driver = self.conf.driver
        driver.find_element_by_xpath("//div[@id='content']//a[.='Edit Account']").click()

    def change_data_in_text_fields(self, form_field, data):
        driver = self.conf.driver
        if data is not None:
            driver.find_element_by_id(form_field).click()
            driver.find_element_by_id(form_field).clear()
            driver.find_element_by_id(form_field).send_keys(data)

    def edit(self, user_data):
        driver = self.conf.driver
        self.open_user_edit_form()
        self.change_data_in_text_fields("input-firstname", user_data.firtsname)
        self.change_data_in_text_fields("input-lastname", user_data.lastname)
        self.change_data_in_text_fields("input-email", user_data.email)
        self.change_data_in_text_fields("input-telephone", user_data.telephone)
        driver.find_element_by_xpath("//form[@class='form-horizontal']/div/div[2]/input").click()