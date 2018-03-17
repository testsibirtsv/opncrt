from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionAssistant
from fixture.address_book import AddressBookAssistant


class Configuration:

    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionAssistant(self)
        self.address_book = AddressBookAssistant(self)

    def open_login_page(self):
        wd = self.wd
        wd.get("http://localhost/opencart/index.php?route=account/login")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def exit_fixture(self):
        self.wd.quit()