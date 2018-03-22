# -*- coding: utf-8 -*-
"""
Contain tests to add address book records.
"""

from operator import attrgetter
from scheme.address_book import AddressBook


def test_add_full_address(conf):
    """
    Create a new address book record and compare the list of records
    on Address Book page before and after creating the address book record.
    """
    entry = AddressBook(first_name="firstname1",
                        last_name="lastname",
                        address_1="address1",
                        address_2="address2",
                        city="city",
                        post_code="postcode",
                        region_state="L'vivs'ka Oblast'",
                        country="Ukraine")
    previous_address_list = conf.address_book.get_content_info_from_list()
    conf.address_book.create(entry)
    updated_address_list = conf.address_book.get_content_info_from_list()
    info_from_new_address = conf.address_book.get_content_info_from_form(entry)
    previous_address_list.append(info_from_new_address)
    assert sorted(previous_address_list, key=attrgetter(
        'content')) == sorted(updated_address_list, key=attrgetter('content'))
