"""
Contain tests to edit address book records.
"""

from scheme.address_book import AddressBook


def test_edit_address_by_position(conf):
    """
    Edit address book record by index.
    """
    index = 0
    record = AddressBook(first_name="edited_firstname",
                         last_name="edited_lastname",
                         company="edited_company",
                         address_1="edited_address1",
                         address_2="edited_address2",
                         city="edited_city",
                         post_code="edited_postcode",
                         country="Ukraine",
                         region_state="Ternopil's'ka Oblast'")
    while conf.address_book.records_count() < index + 1:
        conf.address_book.create(record)
    conf.address_book.edit_record_by_index(record, index)
