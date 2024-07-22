import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.window_width = 1366
    browser.config.window_height = 768
    browser.config.base_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    yield

    browser.quit()
