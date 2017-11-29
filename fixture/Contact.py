from selenium.webdriver.support.ui import Select


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
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        self.change_field_value("lastname", contact.last_name)
        self.select_field_value("bmonth", contact.birth_month)
        self.select_field_value("bday", contact.birth_day)
        self.change_field_value("byear", contact.birth_year)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_group_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_home()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector('input[type="button"][value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.open_home()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home()
        wd.find_element_by_css_selector('img[title="Edit"]').click()
        self.fill_group_form(contact)
        wd.find_element_by_name("update").click()
        self.open_home()

    def count(self):
        self.open_home()
        return len(self.app.wd.find_elements_by_css_selector('img[title="Edit"]'))
