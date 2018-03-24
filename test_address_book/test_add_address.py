# -*- coding: utf-8 -*-
"""
Contain tests to add address book records.
"""

import pytest
from operator import attrgetter
from scheme.address_book import AddressBook


def test_add_new_address(conf):
    """
    Create a new address book record and compare the list of records
    on Address Book page before and after creating the address book record.
    """
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
    with pytest.allure.step(
            "Collect address book list from Address Book page with new record."):
        updated_address_list = conf.address_book.get_content_info_from_list()
    with pytest.allure.step("Take information from new address record."):
        info_from_new_address = conf.address_book.get_content_info_from_form(record)
    with pytest.allure.step("Append info from new record into old list."):
        previous_address_list.append(info_from_new_address)
    with pytest.allure.step("Compare old and new lists."):
        assert sorted(previous_address_list, key=attrgetter(
            'content')) == sorted(updated_address_list, key=attrgetter('content'))
