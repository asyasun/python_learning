from model.Contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name='contact for deletion'))
    app.contact.delete_first_contact()
