from selene.support.shared import browser
from hw_14.pages.manager_page import ManagerPanel
from hw_14.pages.customer_page import CustomerPanel


class Application:
    def __init__(self):
        self.customer_panel = CustomerPanel(self)
        self.manager_panel = ManagerPanel(self)

    def open_browser(self):
        browser.open('')
        return self


app = Application()
