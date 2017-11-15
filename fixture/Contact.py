from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home(self):
        self.app.wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.sec_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        if contact.birth_day > "":
            Select(wd.find_element_by_name("bday")).select_by_value(contact.birth_day)
        if contact.birth_month > "":
            Select(wd.find_element_by_name("bmonth")).select_by_value(contact.birth_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_home()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector('input[type="button"][value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.open_home()

    def edit_first_contact(self):
        wd = self.app.wd
        self.open_home()
        wd.find_element_by_css_selector('img[title="Edit"]').click()
        # Здесь будут какие-то действия по изменению контакта, например...
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("_edited")
        #
        wd.find_element_by_name("update").click()
        self.open_home()
