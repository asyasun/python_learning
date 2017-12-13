from sys import maxsize


class Contact:

    def __init__(self, name=None, sec_name=None, last_name=None, nickname=None, company=None, mobile=None, email=None,
                 birth_day=None, birth_month=None, birth_year=None, contact_id=None):
        self.name = name
        self.sec_name = sec_name
        self.last_name = last_name
        self.nickname = nickname
        self.company = company
        self.mobile = mobile
        self.email = email
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s" % (self.contact_id, self.last_name)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) and \
               self.name == other.name and self.last_name == other.last_name

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
