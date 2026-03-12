import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_experimental_option(
        "prefs",
        {"intl.accept_languages": request.config.getoption("language")}
    )

    if sys.platform.startswith("linux"):
        options.binary_location = "/usr/bin/chromium"
        service = Service(executable_path="/usr/bin/chromedriver")
        browser = webdriver.Chrome(service=service, options=options)
    else:
        browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()