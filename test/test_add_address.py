# -*- coding: utf-8 -*-
from scheme.address_book import AddressBook


def test_add_full_address(conf):
    conf.address_book.create(AddressBook(first_name="firstname", last_name="lastname", company="company", address_1="address1",
                                         address_2="address2", city="city", post_code="postcode",
                                         country="Ukraine", region_state="L'vivs'ka Oblast'"))
