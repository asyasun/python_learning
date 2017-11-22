# -*- coding: utf-8 -*-
from model.Contact import Contact


def test_modify_group_name(app):
    app.contact.edit_first_contact(Contact(name="edited group name"))


def test_modify_group_header(app):
    app.contact.edit_first_contact(Contact(birth_month="December"))
