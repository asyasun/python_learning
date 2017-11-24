# -*- coding: utf-8 -*-
from model.Group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='new group for edit'))
    app.group.edit_first_group(Group(name="edited group name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='new group for edit'))
    app.group.edit_first_group(Group(header="edited group header"))
