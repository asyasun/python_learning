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
        wd.find_element_by_css_selector('input[type="submit"]').click()
                                      # "//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()
        self.app.wd.find_element_by_name("user")

    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_link_text("Logout")) > 0

    def logged_user(self):
        return self.app.wd.find_element_by_xpath('//div/div[1]/form/b').text[1:-1]

    def is_logged_in_as(self, login):
        return self.logged_user() == login

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, login, password):
        if self.is_logged_in():
            if self.is_logged_in_as(login):
                return
            else:
                self.logout()
        self.login(login, password)
