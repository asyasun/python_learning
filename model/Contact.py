from sys import maxsize
from random import choice
from string import digits


class Contact:

    def __init__(self, name=None, sec_name=None, last_name=None, nickname=None, company=None, phone=None, mobile=None,
                 work_phone=None, secondary_phone=None, all_phones_from_homepage=None, email=None, email2=None,
                 email3=None, all_emails=None, birth_day=None, birth_month=None, birth_year=None, address=None,
                 contact_id=None):
        self.name = name
        self.sec_name = sec_name
        self.last_name = last_name
        self.nickname = nickname
        self.company = company
        self.phone = phone
        self.mobile = mobile
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails = all_emails
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.address = address
        self.contact_id = contact_id

    def __repr__(self):
        return "id %s: '%s' '%s'" % (self.contact_id, self.last_name, self.name)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) and \
               self.name == other.name and self.last_name == other.last_name

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize

