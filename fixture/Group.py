class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
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
        self.open_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.open_group_page()

    def edit_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        # Здесь будут какие-то действия по изменению группы, например...
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys("_edited")
        #
        wd.find_element_by_name("update").click()
        self.open_group_page()
