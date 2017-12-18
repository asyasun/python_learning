from model.Group import Group
import random


def test_delete_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name='group for deletion'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)

    app.group.delete_group_by_id(group.group_id)

    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
