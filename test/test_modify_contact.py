# -*- coding: utf-8 -*-
from model.Contact import Contact
import random
from test.different_methods import random_string, random_email, random_phone


def test_modify_contact_name(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(name=random_string('new ', 10)))
    old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)
    edited_contact = Contact(name=random_string('edited ', 10), last_name=contact.last_name, contact_id=contact.contact_id)
    app.contact.edit_contact_by_id(contact.contact_id, edited_contact)

    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(edited_contact)
    print(sorted(new_contacts, key=Contact.id_or_max))
    print(sorted(old_contacts, key=Contact.id_or_max))
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
