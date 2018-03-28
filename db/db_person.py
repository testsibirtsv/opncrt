"""
Contains PersonalDetails class that provides help with
interacting with the Edit Account page.
"""


# class PersonalDetails:
#     """
#     Use to edit user's personal info
#     on the Edit Account page.
#     """
#
#
#
#         def __init__(self, firtsname=None, lastname=None,
#                      email=None, telephone=None):
#             self.firtsname = firtsname
#             self.lastname = lastname
#             self.email = email
#             self.telephone = telephone
#
#         def __repr__(self):
#             return "{} {} {} {}".format(self.firtsname, self.lastname,
#                                         self.email, self.telephone)


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Date, Integer, Numeric
from datetime import date

engine = create_engine('mysql://root@localhost/opencart')
# create_engine('mysql://neo:mysql@localhost/opencart')
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()


class Person(Base):
    __tablename__ = 'oc_customer'

    customer_id = Column(Integer, primary_key=True)
    firstname = Column(String)


    def __init__(self, firstname):
        self.firstname = firstname





def get_people():
    session = session_factory()
    people_query = session.query(Person)
    session.close()
    return people_query.all()


if __name__ == "__main__":
    people = get_people()
    for person in people:
        print(f'{person.firstname}')
