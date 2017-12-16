# -*- coding: utf-8 -*-
from model.Group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='new group for edit'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.edit_group_by_index(index, Group(name="edited group name"))
    assert len(old_groups) == app.group.count()
