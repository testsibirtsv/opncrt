import re
import time
from typing import List
from selenium.webdriver.support.ui import Select
from scheme.address_book import AddressBook


class AddressBookAssistant:

    def __init__(self, conf):
        self.conf = conf

    def create(self, address: AddressBook):
        driver = self.conf.driver
        self.open_address_book_page()
        # start address creation
        self.open_address_book_form_page()
        self.fill_address_form(address)
        # submit address creation
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

    def open_address_book_form_page(self):
        driver = self.conf.driver
        driver.find_element_by_link_text("New Address").click()

    def fill_address_form(self, address: AddressBook):
        self.change_text_field_data("input-firstname", address.first_name)
        self.change_text_field_data("input-lastname", address.last_name)
        self.change_text_field_data("input-company", address.company)
        self.change_text_field_data("input-address-1", address.address_1)
        self.change_text_field_data("input-address-2", address.address_2)
        self.change_text_field_data("input-city", address.city)
        self.change_text_field_data("input-postcode", address.post_code)
        self.change_drop_list_data("input-country", address.country)
        # time.sleep(1)
        self.change_drop_list_data("input-zone", address.region_state)

    def change_drop_list_data(self, ddlist_option: str, value: AddressBook):
        driver = self.conf.driver
        data_select = Select(driver.find_element_by_id(ddlist_option))
        data_select.select_by_visible_text(value)

    def change_text_field_data(self, field_name: str, value: AddressBook):
        driver = self.conf.driver
        if value is not None:
            driver.find_element_by_id(field_name).click()
            driver.find_element_by_id(field_name).clear()
            driver.find_element_by_id(field_name).send_keys(value)

    def open_address_book_page(self):
        driver = self.conf.driver
        if driver.current_url.endswith("account/address"):
            return
        driver.find_element_by_link_text("Address Book").click()

    def delete_entry_by_index(self, index: int):
        driver = self.conf.driver
        self.open_address_book_page()
        driver.find_elements_by_xpath(
            "//div[@class='table-responsive']//a[.='Delete']")[index].click()

    def edit_entry_by_index(self, updated_values: AddressBook, index: int):
        driver = self.conf.driver
        self.open_address_book_page()
        self.open_edit_page_by_position(index)
        # fill form with new data
        self.fill_address_form(updated_values)
        # accept changed data
        driver.find_element_by_xpath("//form[@class='form-horizontal']/div/div[2]/input").click()

    def open_edit_page_by_position(self, position: int):
        driver = self.conf.driver
        driver.find_elements_by_xpath(
            "//div[@class='table-responsive']//a[.='Edit']")[position].click()

    def get_address_book_info(self) -> List[AddressBook]:
        driver = self.conf.driver
        self.open_address_book_page()
        address_list = []
        for line in driver.find_elements_by_xpath('//*[@id="content"]//table/tbody//td[1]'):
            content = re.sub(r'\s', '', line.text)
            address_list.append(AddressBook(content=content))
        return address_list

    def get_info_from_address_form(self, address_obj: AddressBook) -> AddressBook:
        self.open_address_book_page()
        info_from_object = []
        for attr in address_obj.__dict__.items():
            if attr[1] is not None:
                info_from_object.append(attr[1])
        content = re.sub(r'\s', '', "".join(info_from_object))
        return AddressBook(content=content)

    def entries_count(self):
        driver = self.conf.driver
        self.open_address_book_page()
        return len(driver.find_elements_by_xpath(
            "//div[@class='table-responsive']//a[.='Edit']"))
