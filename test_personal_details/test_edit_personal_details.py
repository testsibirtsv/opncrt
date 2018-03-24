"""Temp info."""
from scheme.personal_details import PersonalDetails


def test_edit_user_info(conf):
    conf.personal_details.edit(PersonalDetails(firtsname="Serhii",
                                               lastname="TestLastName",
                                               email="taqc296@gmail.com",
                                               telephone="12345"))
