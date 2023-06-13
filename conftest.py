import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language is not None:
        options = Options()
        options.add_experimental_option("prefs", {"init.accept_language": user_language})
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    return user_language