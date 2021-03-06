from selenium.webdriver.support.ui import Select
from model.Contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home(self):
        wd = self.app.wd
        if wd.current_url.endswith('addressbook/') and self.app.session.is_logged_in():
            return
        wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_field_value(self, field_name, value):
        if value is not None:
            Select(self.app.wd.find_element_by_name(field_name)).select_by_value(value)

    def fill_group_form(self, contact):
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.sec_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.select_field_value("bmonth", contact.birth_month)
        self.select_field_value("bday", contact.birth_day)
        self.change_field_value("byear", contact.birth_year)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_group_form(contact)
        wd.find_element_by_xpath('//div[@id="content"]/form/input[21]').click()
        self.open_home()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home()

        wd.find_elements_by_name('selected[]')[index].click()
        wd.find_element_by_css_selector('input[type="button"][value="Delete"]').click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")

        self.open_home()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_for_edit_by_index(index)
        self.fill_group_form(contact)
        wd.find_element_by_name("update").click()

        self.open_home()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_for_edit_by_id(id)
        self.fill_group_form(contact)
        wd.find_element_by_name("update").click()

        self.open_home()
        self.contact_cache = None

    def open_contact_for_edit_by_index(self, index):
        self.open_home()
        self.app.wd.find_elements_by_css_selector('img[title="Edit"]')[index].click()

    def open_contact_for_edit_by_id(self, id):
        self.open_home()
        self.app.wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def open_contact_view_by_index(self, index):
        self.open_home()
        self.app.wd.find_elements_by_css_selector('img[title="Details"]')[index].click()

    def count(self):
        self.open_home()
        return len(self.app.wd.find_elements_by_css_selector('img[title="Edit"]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                texts = element.find_elements_by_tag_name('td')

                contact_id = texts[0].find_element_by_tag_name('input').get_attribute('value')
                last_name = texts[1].text
                name = texts[2].text
                all_phones = texts[5].text
                email_elements = texts[4].find_elements_by_css_selector('a')
                all_emails = []
                for email in email_elements:
                    all_emails.append(email.text)
                address = texts[3].text

                self.contact_cache.append(Contact(name=name, last_name=last_name, contact_id=contact_id,
                                                  all_phones_from_homepage=all_phones,
                                                  all_emails=' '.join(all_emails), address=address))

        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_for_edit_by_index(index)
        wd = self.app.wd

        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')

        phone = wd.find_element_by_name('home').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        mobile = wd.find_element_by_name('mobile').get_attribute('value')
        secondary_phone = wd.find_element_by_name('phone2').get_attribute('value')

        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')

        return Contact(name=firstname, last_name=lastname, contact_id=id, phone=phone,
                       work_phone=work_phone, mobile=mobile, secondary_phone=secondary_phone,
                       email=email1, email2=email2, email3=email3, address=address)

    def get_contact_info_from_view_page(self, index):
        self.open_contact_view_by_index(index)
        wd = self.app.wd
        text = wd.find_element_by_id('content').text
        phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(phone=phone, work_phone=work_phone, mobile=mobile, secondary_phone=secondary_phone)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home()

        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_css_selector('input[type="button"][value="Delete"]').click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")

        self.open_home()
        self.contact_cache = None
