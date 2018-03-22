"""Some information"""
from scheme.address_book import AddressBook


def test_delete_address_book_entry(conf):
    if conf.address_book.entries_count() <= 2:
        conf.address_book.create(AddressBook(first_name="firstname1",
                                             last_name="lastname",
                                             address_1="address1",
                                             address_2="address2",
                                             city="city",
                                             post_code="postcode",
                                             region_state="L'vivs'ka Oblast'",
                                             country="Ukraine"))
    previous_address_list = conf.address_book.get_address_book_info()
    conf.address_book.delete_entry_by_index(1)
    updated_address_list = conf.address_book.get_address_book_info()
    assert len(previous_address_list) - 1 == len(updated_address_list)
