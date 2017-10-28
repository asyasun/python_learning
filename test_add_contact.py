# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import unittest
from Contact import Contact
from Common import *


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    @staticmethod
    def add_new_contact(wd, contact):
        ActionChains(wd).double_click(wd.find_element_by_link_text("add new")).perform()
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
        if contact.burth_day > "":
            Select(wd.find_element_by_name("bday")).select_by_value(contact.burth_day)
        if contact.burth_month > "":
            Select(wd.find_element_by_name("bmonth")).select_by_value(contact.burth_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.burth_year)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def test_add_contact(self):
        wd = self.wd
        Common.open_homepage(wd)
        Common.login(wd, login="admin", password="secret")
        self.add_new_contact(wd, Contact(name="Ivan", sec_name="Ivanovich", last_name="Ivanov", nick="Ivs",
                                         company="OOO software", mobile="9875634", email="ivan@ivan.ru",
                                         burth_day="15", burth_month="June", burth_year="1988"))
        Common.open_home(wd)
        Common.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        Common.open_homepage(wd)
        Common.login(wd, login="admin", password="secret")
        self.add_new_contact(wd, Contact(name="", sec_name="", last_name="", nick="",
                                         company="", mobile="", email="",
                                         burth_day="", burth_month="", burth_year=""))
        Common.open_home(wd)
        Common.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
