# -*- coding: utf-8 -*-
from operator import attrgetter
import pytest
from scheme.address_book import AddressBook


def test_add_new_address(conf):
    record = AddressBook(first_name="firstname1",
                         last_name="lastname",
                         address_1="address1",
                         address_2="address2",
                         city="city",
                         post_code="postcode",
                         region_state="L'vivs'ka Oblast'",
                         country="Ukraine")
    with pytest.allure.step("Collect address book list from Address Book page."):
        previous_address_list = conf.address_book.get_content_info_from_list()
    with pytest.allure.step("Create new address book record."):
        conf.address_book.create(record)
    with pytest.allure.step("Collect address book list from Address Book page with new record."):
        updated_address_list = conf.address_book.get_content_info_from_list()
    with pytest.allure.step("Take information from new address record."):
        info_from_new_address = conf.address_book.get_content_info_from_form(record)
    with pytest.allure.step("Append info from new record into old list."):
        previous_address_list.append(info_from_new_address)
    with pytest.allure.step("Retrieving info about successfully added address."):
        assert conf.address_book.get_alert_message() == 'Your address has been successfully added'
    with pytest.allure.step("Compare old and new lists."):
        assert sorted(previous_address_list, key=attrgetter(
            'content')) == sorted(updated_address_list, key=attrgetter('content'))


# def test_add_incorrect_address(conf):
#     conf.address_book.create(AddressBook(address_1="ad",
#                                          city="c",
#                                          post_code="p"))
#     conf.address_book.get_form_error_messages()
