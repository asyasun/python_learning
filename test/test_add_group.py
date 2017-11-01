# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application
from model.Group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(login="admin", password="secret")
    app.add_group(Group(name="test group 1", header="header", footer="footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(login="admin", password="secret")
    app.add_group(Group(name="", header="", footer=""))
    app.session.logout()

