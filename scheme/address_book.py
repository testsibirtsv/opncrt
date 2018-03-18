from sys import maxsize


class AddressBook:

    def __init__(self, first_name=None,
                 last_name=None,
                 company=None,
                 address_1=None,
                 address_2=None,
                 city=None,
                 post_code=None,
                 country=None,
                 region_state=None,
                 id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.post_code = post_code
        self.country = country
        self.region_state = region_state
        self.id = id

    def __repr__(self):
        return "{}".format(self.id)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id

    def get_id_value(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
