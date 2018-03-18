# -*- coding: utf-8 -*-
from scheme.address_book import AddressBook


def test_add_full_address(conf):
    previous_address_list = conf.address_book.get_address_list()
    address_entry = AddressBook(first_name="firstname",
                                last_name="lastname",
                                company="company",
                                address_1="address1",
                                address_2="address2",
                                city="city",
                                post_code="postcode",
                                country="Ukraine",
                                region_state="L'vivs'ka Oblast'")
    conf.address_book.create(address_entry)
    updated_address_list = conf.address_book.get_address_list()
    assert len(previous_address_list) + 1 == len(updated_address_list)
    previous_address_list.append(address_entry)
    assert sorted(previous_address_list, key=AddressBook.get_id_value) == sorted(updated_address_list, key=AddressBook.get_id_value)
