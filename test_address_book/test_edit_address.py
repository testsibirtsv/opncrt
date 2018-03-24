"""
Contain tests to edit address book records.
"""

from scheme.address_book import AddressBook


def test_edit_address_by_index(conf):
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
                         post_code="e_postcode",
                         country="Ukraine",
                         region_state="Ternopil's'ka Oblast'")
    while conf.address_book.records_count() < index + 1:
        conf.address_book.create(record)
    conf.address_book.edit_record_by_index(record, index)
    info_from_edited_address = conf.address_book.get_content_info_from_form(record)
    updated_info_from_address_list = conf.address_book.get_content_info_by_index(index)
    assert info_from_edited_address == updated_info_from_address_list
