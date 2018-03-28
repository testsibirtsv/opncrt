"""
Contains PersonalDetails class that provides help with
interacting with the Edit Account page.
"""


class PersonalDetails:
    """
    Use to edit user's personal info
    on the Edit Account page.
    """

    def __init__(self, firtsname=None, lastname=None,
                 email=None, telephone=None):
        self.firtsname = firtsname
        self.lastname = lastname
        self.email = email
        self.telephone = telephone

    def __repr__(self):
        return "{} {} {} {}".format(self.firtsname, self.lastname,
                                    self.email, self.telephone)
