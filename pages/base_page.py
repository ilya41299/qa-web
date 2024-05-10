from selenium.webdriver import Remote

from config import settings

from page_components.page_interface.page_interface import PageInterface


class BasePage:
    def __init__(self, driver: Remote):
        self.page_interface = PageInterface(driver)
        self.url = settings.base_url

    def open_page(self):
        self.page_interface.visit(self.url)

    def visit_url(self, url: str):
        self.page_interface.visit(url)

    def reload_page(self):
        self.page_interface.reload()
