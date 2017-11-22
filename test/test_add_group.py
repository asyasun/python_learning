# -*- coding: utf-8 -*-
from model.Group import Group


def test_add_group(app):
    app.group.create(Group(name="test group 1", header="header", footer="footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

