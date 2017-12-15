# -*- coding: utf-8 -*-
from model.Contact import Contact
import pytest
from test.different_methods import random_string, random_email, random_phone


test_data = [Contact(name="", sec_name="", last_name="", nickname="", company="", phone="",
                     mobile="", work_phone="", secondary_phone="", email="")] + [
             Contact(name=random_string('', 10), sec_name=random_string('', 10),
                     last_name=random_string('', 20), nickname=random_string('', 15),
                     company=random_string('', 25), phone=random_phone(), mobile=random_phone(),
                     work_phone=random_phone(), secondary_phone=random_phone(), email=random_email())
             for i in range(5)
]


@pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
