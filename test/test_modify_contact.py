# -*- coding: utf-8 -*-
from model.Contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name='new contact for edit'))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(name="edited contact name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_birth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name='new contact for edit'))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(birth_month="December"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
