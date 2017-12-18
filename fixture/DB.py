import pymysql
from model.Group import Group
from model.Contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (group_id, name, header, footer) = row
                groups.append(Group(group_id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups

    def get_contact_list(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname from addressbook')
            for row in cursor:
                (contact_id, name, last_name) = row
                contacts.append(Contact(contact_id=str(contact_id), name=name, last_name=last_name))
        finally:
            cursor.close()
        return contacts
