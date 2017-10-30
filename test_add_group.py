# -*- coding: utf-8 -*-
import pytest
from Group import Group
from Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(login="admin", password="secret")
    app.add_group(Group(name="test group 1", header="header", footer="footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(login="admin", password="secret")
    app.add_group(Group(name="", header="", footer=""))
    app.logout()

