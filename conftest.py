import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption("--language", action = "store", default = "en",
                      help = "choose language: 'ru' or 'en'..")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for a test..")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nclose browser")
    browser.quit()