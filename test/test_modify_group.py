# -*- coding: utf-8 -*-
from model.Group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name='new group for edit'))
    old_groups = app.group.get_group_list()

    group = random.choice(old_groups)
    edited_group = Group(name="edited group name", header=group.header, footer=group.footer, group_id=group.group_id)
    app.group.edit_group_by_id(group.group_id, edited_group)

    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(edited_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
