import time

from selene import browser, have


class CustomerPanel:

    def __init__(self, app):
        self.login_button_element = browser.all('.btn-primary')
        self.select_element = browser.element('#userSelect').all('option')[4]
        self.submit_button_element = browser.element('[type = "submit"]')
        self.deposit_button_element = browser.element('button[ng-click="deposit()"]')
        self.amount_element = browser.element('input[ng-model="amount"]')
        self.message_element = browser.element('span.error.ng-binding')
        self.withdrawn_button_element = browser.element('button[ng-click="withdrawl()"]')
        self.message_element = browser.element('span.error.ng-binding')

        self.app = app

    def login(self):
        self.login_button_element.element_by(have.text("Customer Login")).click()
        self.select_element.click()
        self.submit_button_element.click()

    def open_customer_form(self):
        self.app.open_browser()
        self.login()

    def withdrawn(self, value):
        self.withdrawn_button_element.click()
        time.sleep(2)
        self.amount_element.set_value(value)
        self.submit_button_element.click()
        self.message_element.should(have.text('Transaction successful'))

    def add_deposit(self, value):
        self.deposit_button_element.click()
        self.amount_element.set_value(value)
        self.submit_button_element.click()
        self.message_element.should(have.text('Deposit Successful'))
