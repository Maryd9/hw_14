from selene import browser, have, be


class ManagerPanel:
    def __init__(self, app):
        self.login_button_element = browser.all('.btn-primary')
        self.add_button_element = browser.all('.btn-lg')
        self.first_name_element = browser.element('.form-control[placeholder="First Name"]')
        self.last_name_element = browser.element('.form-control[placeholder="Last Name"]')
        self.post_code_element = browser.element('.form-control[placeholder="Post Code"]')
        self.search_element = browser.element('.form-control')
        self.table_element = browser.element('tr.ng-scope')
        self.result_1_element = browser.element('td.ng-binding:nth-child(1)')
        self.result_2_element = browser.element('td.ng-binding:nth-child(2)')
        self.result_3_element = browser.element('td.ng-binding:nth-child(3)')
        self.button_delete_element = browser.element('button[ng-click="deleteCust(cust)"]')
        self.customer_element = browser.element('#userSelect').all('option')[4]
        self.currency_element = browser.element('#currency').all('option')[2]
        self.process_button_element = browser.element('[type = "submit"]')
        self.app = app

    def login(self):
        self.login_button_element.element_by(have.text("Bank Manager Login")).click()

    def open_manager_form(self):
        self.app.open_browser()
        self.login()

    def add_new_customer(self, first_name, last_name, post_code):
        self.add_button_element.element_by(have.text("Add Customer")).click()
        self.first_name_element.type(first_name)
        self.last_name_element.type(last_name)
        self.post_code_element.type(post_code).press_enter()
        alert = browser.driver.switch_to.alert
        alert.accept()

    def open_account(self):
        self.add_button_element.element_by(have.text("Open Account")).click()
        self.customer_element.click()
        self.currency_element.click()
        self.process_button_element.click()
        alert = browser.driver.switch_to.alert
        alert.accept()

    def search_customer(self, first_name):
        self.add_button_element.element_by(have.text("Customers")).click()
        self.search_element.type(first_name).press_enter()

    def check_customer(self, first_name, last_name, post_code):
        self.result_1_element.should(have.text(first_name))
        self.result_2_element.should(have.text(last_name))
        self.result_3_element.should(have.text(post_code))

    def delete_customer(self):
        self.button_delete_element.click()
        self.table_element.should(be.not_.present)
