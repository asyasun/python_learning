class Common:

    @staticmethod
    def open_homepage(wd):
        wd.get("http://localhost/addressbook/")

    @staticmethod
    def login(wd, login, password):
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

    @staticmethod
    def logout(wd):
        wd.find_element_by_link_text("Logout").click()

    @staticmethod
    def open_home(wd):
        wd.find_element_by_link_text("home").click()