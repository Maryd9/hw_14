import allure
from hw_14.pages.application import app


@allure.title("Add deposit")
def test_add_deposit():
    with allure.step("Open customer form"):
        app.customer_panel.open_customer_form()
    with allure.step("Open add deposit"):
        app.customer_panel.add_deposit('6000')


@allure.title("Withdrawn")
def test_withdrawn():
    with allure.step("Open customer form"):
        app.customer_panel.open_customer_form()
    with allure.step("Open add deposit"):
        app.customer_panel.add_deposit('10000')
    with allure.step("Withdrawn"):
        app.customer_panel.withdrawn('2444')
