# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application
from model.Contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.sesion.login(login="admin", password="secret")
    app.contact.create(Contact(name="Ivan", sec_name="Ivanovich", last_name="Ivanov", nick="Ivs",
                               company="OOO software", mobile="9875634", email="ivan@ivan.ru",
                               birth_day="15", birth_month="June", birth_year="1988"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact(name="", sec_name="", last_name="", nick="",
                               company="", mobile="", email="",
                               birth_day="", birth_month="", birth_year=""))
    app.session.logout()

