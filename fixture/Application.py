from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.Session import SessionHelper
from fixture.Group import GroupHelper
from fixture.Contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_homepage(self):
        self.wd.get("http://localhost/addressbook/")