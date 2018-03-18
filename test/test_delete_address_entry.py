from scheme.address_book import AddressBook


def test_delete_first_entry(conf):
    if conf.address_book.amount() == 0:
        conf.address_book.create(
            AddressBook(first_name="firstname",
                        last_name="lastname",
                        company="company",
                        address_1="address1",
                        address_2="address2",
                        city="city",
                        post_code="postcode",
                        country="Ukraine",
                        region_state="L'vivs'ka Oblast'"))
    previous_address_list = conf.address_book.get_address_list()
    conf.address_book.delete_first_entry()
    updated_address_list = conf.address_book.get_address_list()
    assert len(previous_address_list) - 1 == len(updated_address_list)
    previous_address_list[0:1] = []
    assert previous_address_list == updated_address_list
