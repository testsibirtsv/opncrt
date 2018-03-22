"""Temp information"""


class AddressBook:

    def __init__(self, first_name=None,
                 last_name=None,
                 company=None,
                 address_1=None,
                 address_2=None,
                 city=None,
                 post_code=None,
                 region_state=None,
                 country=None,
                 content=None,
                 id=None,
                 zone_id=None,
                 country_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.post_code = post_code
        self.region_state = region_state
        self.country = country
        self.content = content
        self.id = id
        self.zone_id = zone_id
        self.country_id = country_id

    def __repr__(self):
        return "{} {} {} {}".format(self.first_name,
                                    self.last_name,
                                    self.content,
                                    self.id)

    def __eq__(self, other):
        return self.content == other.content
