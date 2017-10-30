# -*- coding: utf-8 -*-
import pytest
from Contact import Contact
from Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(login="admin", password="secret")
    app.add_new_contact(Contact(name="Ivan", sec_name="Ivanovich", last_name="Ivanov", nick="Ivs",
                                company="OOO software", mobile="9875634", email="ivan@ivan.ru",
                                birth_day="15", birth_month="June", birth_year="1988"))
    app.logout()


def test_add_empty_contact(app):
    app.login(login="admin", password="secret")
    app.add_new_contact(Contact(name="", sec_name="", last_name="", nick="",
                                company="", mobile="", email="",
                                birth_day="", birth_month="", birth_year=""))
    app.logout()

