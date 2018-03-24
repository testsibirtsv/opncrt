"""
Contain tests to delete address book records.
"""

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
    previous_address_list = conf.address_book.get_content_info_from_list()
    conf.address_book.delete_record_by_index(index)
    updated_address_list = conf.address_book.get_content_info_from_list()
    assert len(previous_address_list) - 1 == len(updated_address_list)
