from model.Group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith('group.php') and len(wd.find_elements_by_name('new')) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init creation of the new group
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # finalize
        wd.find_element_by_name("submit").click()
        self.open_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()

        wd.find_elements_by_name("selected[]")[index].click()

        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()

        wd.find_element_by_css_selector("input[value='%s']" % id).click()

        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def edit_first_group(self, new_group_data):
        self.edit_group_by_index(0, new_group_data)

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("edit").click()

        self.fill_group_form(new_group_data)

        wd.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

    def edit_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_group_page()

        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("edit").click()

        self.fill_group_form(new_group_data)

        wd.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

    def count(self):
        self.open_group_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                group_id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, group_id=group_id))

        return list(self.group_cache)
