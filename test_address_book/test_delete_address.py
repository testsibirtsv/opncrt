"""
Contain tests to delete address book records.
"""

import pytest
from scheme.address_book import AddressBook


def test_delete_address_book_record_by_index(conf):
    """
    Delete the address book record by index and compare the length
    of the record list before and after deleting the address book record.
    """
    index = 0
    while conf.address_book.records_count() < index + 1:
        conf.address_book.create(AddressBook(first_name="firstname1",
                                             last_name="lastname_1",
                                             address_1="address1_2",
                                             address_2="address2_3",
                                             city="city",
                                             post_code="postcode",
                                             region_state="L'vivs'ka Oblast'",
                                             country="Ukraine"))
    with pytest.allure.step("Take the number of address book records on the page."):
        previous_address_list = len(conf.address_book.get_content_info_from_list())
    with pytest.allure.step("Delete address book record by index %d." % index):
        conf.address_book.delete_record_by_index(index)
    with pytest.allure.step(
            "Take len of address list after deleting the record by index %d" % index):
        updated_address_list = len(conf.address_book.get_content_info_from_list())
    with pytest.allure.step("Compare the length of the list before and after deleting the record"):
        assert previous_address_list - 1 == updated_address_list
