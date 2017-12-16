import re
import random

#
# def test_phones_homepage_vs_edit_page(app):
#     contact_from_homepage = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#
#     assert contact_from_homepage.all_phones_from_homepage == merge_phones(contact_from_edit_page)


def merge_phones(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phone, contact.work_phone, contact.mobile, contact.secondary_phone]))))


def test_phones_view_page_vs_edit_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)

    assert contact_from_view_page.phone == contact_from_edit_page.phone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def clear(s):
    return re.sub("[() -]", '', s)


def merge_emails(contact):
    return ' '.join(filter(lambda x: x != '' and x != ' ', [contact.email, contact.email2, contact.email3]))


def test_homepage_vs_edit_page(app):
    contact_for_check = random.randrange(app.contact.count())

    contact_from_homepage = app.contact.get_contact_list()[contact_for_check]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_for_check)

    assert contact_from_homepage.name == contact_from_edit_page.name
    assert contact_from_homepage.last_name == contact_from_edit_page.last_name
    assert contact_from_homepage.address == contact_from_edit_page.address

    assert contact_from_homepage.all_emails == merge_emails(contact_from_edit_page)

    assert contact_from_homepage.all_phones_from_homepage == merge_phones(contact_from_edit_page)
