class SessionAssistant:

    def __init__(self, conf):
        self.conf = conf

    def login(self, email, password):
        wd = self.conf.wd
        self.conf.open_login_page()
        wd.find_element_by_id("input-email").click()
        wd.find_element_by_id("input-email").clear()
        wd.find_element_by_id("input-email").send_keys(email)
        wd.find_element_by_id("input-password").click()
        wd.find_element_by_id("input-password").clear()
        wd.find_element_by_id("input-password").send_keys(password)
        wd.find_element_by_css_selector("input.btn.btn-primary").click()

    def logout(self):
        wd = self.conf.wd
        wd.find_element_by_xpath("//ul[@class='list-inline']//a[.=' My Account ']").click()
        wd.find_element_by_xpath("//ul[@class='list-inline']//a[.='Logout']").click()

    def check_logout(self):
        wd = self.conf.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.conf.wd
        return len(wd.find_elements_by_xpath("//ul[@class='list-inline']//a[.='Logout']")) > 0

    def check_login(self, email, password):
        wd = self.conf.wd
        if self.is_logged_in():
                return
        self.login(email, password)
