from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionAssistant
from fixture.address_book import AddressBookAssistant


class Configuration:

    def __init__(self):
        self.driver = WebDriver()
        self.session = SessionAssistant(self)
        self.address_book = AddressBookAssistant(self)

    def open_login_page(self):
        driver = self.driver
        driver.get("http://localhost/opencart/index.php?route=account/login")

    def exit_fixture(self):
        self.driver.quit()
