# -*- coding: utf-8 -*-
from model.Group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='new group for edit'))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="edited group name"))
    assert len(old_groups) == app.group.count()


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='new group for edit'))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="edited group header"))
    assert len(old_groups) == app.group.count()
