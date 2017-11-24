from model.Group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='group for deletion'))
    app.group.delete_first_group()

