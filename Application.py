from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def destroy(self):
        self.wd.quit()

    def open_homepage(self):
        self.wd.get("http://localhost/addressbook/")

    def login(self, login, password):
        self.open_homepage()
        # open login form
        self.wd.find_element_by_id("LoginForm").click()
        # user enter
        self.wd.find_element_by_name("user").click()
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(login)
        # password enter
        self.wd.find_element_by_name("pass").click()
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def open_home(self):
        self.wd.find_element_by_link_text("home").click()

    def add_group(self, group):
        self.wd.find_element_by_link_text("groups").click()
        # init creation of the new group
        self.wd.find_element_by_name("new").click()
        # group name enter
        self.wd.find_element_by_name("group_name").click()
        self.wd.find_element_by_name("group_name").clear()
        self.wd.find_element_by_name("group_name").send_keys(group.name)
        # group header enter
        self.wd.find_element_by_name("group_header").click()
        self.wd.find_element_by_name("group_header").clear()
        self.wd.find_element_by_name("group_header").send_keys(group.header)
        # group footer enter
        self.wd.find_element_by_name("group_footer").click()
        self.wd.find_element_by_name("group_footer").clear()
        self.wd.find_element_by_name("group_footer").send_keys(group.footer)
        # finalize
        self.wd.find_element_by_name("submit").click()
        self.wd.find_element_by_link_text("groups").click()

    def add_new_contact(self, contact):
        self.wd.find_element_by_link_text("add new").click()
        self.wd.find_element_by_name("firstname").click()
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.name)
        self.wd.find_element_by_name("middlename").click()
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.sec_name)
        self.wd.find_element_by_name("lastname").click()
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.last_name)
        self.wd.find_element_by_name("nickname").click()
        self.wd.find_element_by_name("nickname").clear()
        self.wd.find_element_by_name("nickname").send_keys(contact.nick)
        self.wd.find_element_by_name("company").click()
        self.wd.find_element_by_name("company").clear()
        self.wd.find_element_by_name("company").send_keys(contact.company)
        self.wd.find_element_by_name("mobile").click()
        self.wd.find_element_by_name("mobile").clear()
        self.wd.find_element_by_name("mobile").send_keys(contact.mobile)
        self.wd.find_element_by_name("fax").click()
        self.wd.find_element_by_name("email").click()
        self.wd.find_element_by_name("email").clear()
        self.wd.find_element_by_name("email").send_keys(contact.email)
        if contact.birth_day > "":
            Select(self.wd.find_element_by_name("bday")).select_by_value(contact.birth_day)
        if contact.birth_month > "":
            Select(self.wd.find_element_by_name("bmonth")).select_by_value(contact.birth_month)
        self.wd.find_element_by_name("byear").click()
        self.wd.find_element_by_name("byear").clear()
        self.wd.find_element_by_name("byear").send_keys(contact.birth_year)
        self.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_home()
