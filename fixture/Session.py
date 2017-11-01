class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        self.app.open_homepage()
        # open login form
        wd.find_element_by_id("LoginForm").click()
        # user enter
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        # password enter
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()
