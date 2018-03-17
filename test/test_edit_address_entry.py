from scheme.address_book import AddressBook


def test_edit_full_address(conf):
    if conf.address_book.amount() == 0:
        conf.address_book.create(
            AddressBook(first_name="firstname", last_name="lastname", company="company", address_1="address1",
                        address_2="address2", city="city", post_code="postcode",
                        country="Ukraine", region_state="L'vivs'ka Oblast'"))
    conf.address_book.edit_first_entry(AddressBook(first_name="edited_firstname", last_name="edited_lastname", company="edited_company", address_1="edited_address1",
                                         address_2="edited_address2", city="edited_city", post_code="edited_postcode",
                                         country="Ukraine", region_state="Ternopil's'ka Oblast'"))
