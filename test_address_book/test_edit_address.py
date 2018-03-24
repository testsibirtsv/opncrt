"""
Contain tests to edit address book records.
"""

from scheme.address_book import AddressBook


def test_edit_address_by_position(conf):
    """
    Edit address book record by index.
    """
    conf.address_book.edit_entry_by_index(AddressBook(first_name="edited_firstname",
                                                      last_name="edited_lastname",
                                                      company="edited_company",
                                                      address_1="edited_address1",
                                                      address_2="edited_address2",
                                                      city="edited_city",
                                                      post_code="edited_postcode",
                                                      country="Ukraine",
                                                      region_state="Ternopil's'ka Oblast'"),
                                          0)
