import allure
from hw_14.data.users import user
from hw_14.pages.application import app


@allure.title("Add customer")
def test_add_customer():
    with allure.step("Open manager form"):
        app.manager_panel.open_manager_form()
    with allure.step("Add customer"):
        app.manager_panel.add_new_customer(user.first_name, user.last_name, user.post_code)


@allure.title("Open account")
def test_open_account():
    with allure.step("Open manager form"):
        app.manager_panel.open_manager_form()
    with allure.step("Open account"):
        app.manager_panel.open_account()


@allure.title("Search customer")
def test_search_customer():
    with allure.step("Open manager form"):
        app.manager_panel.open_manager_form()
    with allure.step("Search customer"):
        app.manager_panel.search_customer('Neville')
    with allure.step("Check customer"):
        app.manager_panel.check_customer('Neville', 'Longbottom', 'E89898')


@allure.title("Delete customer")
def test_delete_customer():
    with allure.step("Open manager form"):
        app.manager_panel.open_manager_form()
    with allure.step("Search customer"):
        app.manager_panel.search_customer('Neville')
    with allure.step("Delete customer"):
        app.manager_panel.delete_customer()
