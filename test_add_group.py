# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from Group import Group
from Common import *


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    @staticmethod
    def add_group(wd, group):
        # init creation of the new group
        wd.find_element_by_name("new").click()
        # group name enter
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        # group header enter
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        # group footer enter
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # finalize
        wd.find_element_by_name("submit").click()

    @staticmethod
    def open_groups(wd):
        wd.find_element_by_link_text("groups").click()

    def tearDown(self):
        self.wd.quit()

    def test_add_group(self):
        wd = self.wd
        Common.open_homepage(wd)
        Common.login(wd, login="admin", password="secret")
        self.open_groups(wd)
        self.add_group(wd, Group(name="test group 1", header="header", footer="footer"))
        self.open_groups(wd)
        Common.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        Common.open_homepage(wd)
        Common.login(wd, login="admin", password="secret")
        self.open_groups(wd)
        self.add_group(wd, Group(name="", header="", footer=""))
        self.open_groups(wd)
        Common.logout(wd)


if __name__ == '__main__':
    unittest.main()
