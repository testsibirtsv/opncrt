"""
Temp info.
"""


class PersonalDetails:

    def __init__(self, firtsname=None, lastname=None,
                 email=None, telephone=None):
        self.firtsname = firtsname
        self.lastname = lastname
        self.email = email
        self.telephone = telephone

    def __repr__(self):
        return "{} {} {} {}".format(self.firtsname, self.lastname,
                                    self.email, self.telephone)
