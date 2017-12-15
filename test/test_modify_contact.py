# -*- coding: utf-8 -*-
from model.Contact import Contact
from random import randrange
from test.different_methods import random_string, random_email, random_phone


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name=random_string('new ', 10)))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.edit_contact_by_index(index, Contact(name=random_string('edited ', 10)))
    assert len(old_contacts) == app.contact.count()


# def test_modify_contact_birth(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name='new contact for edit'))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.contact.edit_contact_by_index(index, Contact(birth_month='December'))
#     assert len(old_contacts) == app.contact.count()
