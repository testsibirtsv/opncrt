from selenium.webdriver.support.ui import Select


class AddressBookAssistant:

    def __init__(self, conf):
        self.conf = conf

    def create(self, address):
        wd = self.conf.wd
        self.open_address_book_page()
        # start address creation
        wd.find_element_by_link_text("New Address").click()
        self.fill_address_form(address)
        # submit address creation
        wd.find_element_by_css_selector("input.btn.btn-primary").click()

    def fill_address_form(self, address):
        wd = self.conf.wd
        self.change_text_field_data("input-firstname", address.first_name)
        self.change_text_field_data("input-lastname", address.last_name)
        self.change_text_field_data("input-company", address.company)
        self.change_text_field_data("input-address-1", address.address_1)
        self.change_text_field_data("input-address-2", address.address_2)
        self.change_text_field_data("input-city", address.city)
        self.change_text_field_data("input-postcode", address.post_code)
        self.change_drop_list_data("input-country", address.country)
        self.change_drop_list_data("input-zone", address.region_state)

    def change_drop_list_data(self, ddlist_option, value):
        wd = self.conf.wd
        data_select = Select(wd.find_element_by_id(ddlist_option))
        data_select.select_by_visible_text(value)

    def change_text_field_data(self, field_name, value):
        wd = self.conf.wd
        if value is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(value)

    def open_address_book_page(self):
        wd = self.conf.wd
        wd.find_element_by_link_text("Address Book").click()

    def delete_first_entry(self):
        wd = self.conf.wd
        self.open_address_book_page()
        wd.find_elements_by_xpath("//div[@class='table-responsive']//a[.='Delete']")[0].click()

    def edit_first_entry(self, updated_values):
        wd = self.conf.wd
        self.open_address_book_page()
        # open address form
        wd.find_elements_by_xpath("//div[@class='table-responsive']//a[.='Edit']")[0].click()
        # fill form with new data
        self.fill_address_form(updated_values)
        # accept changed data
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div/div[2]/input").click()

    def amount(self):
        wd = self.conf.wd
        self.open_address_book_page()
        return len(wd.find_elements_by_xpath("//div[@class='table-responsive']//a[.='Delete']"))

