# -*- coding: utf-8 -*-
from model.Contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Ivan", sec_name="Ivanovich", last_name="Ivanov", nickname="Ivs",
                               company="OOO software", mobile="9875634", email="ivan@ivan.ru",
                               birth_day="15", birth_month="June", birth_year="1988")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="", sec_name="", last_name="", nickname="",
                               company="", mobile="", email="",
                               birth_day="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
