# -*- coding: utf-8 -*-
from model.Group import Group
import pytest
from test.different_methods import random_string


test_data = [Group(name="", header="", footer="")] + [
             Group(name=random_string('name', 10), header=random_string('header', 20), footer=random_string('footer', 20))
             for i in range(5)
]


@pytest.mark.parametrize('group', test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
