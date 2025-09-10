# tests/conftest.py
import os, sys
#adding current dir to sys path to avoid module not found error
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    d = get_driver()
    yield d
    d.quit()

#@pytest.fixture(scope="function")
#def wait(driver):
#    return WebDriverWait(driver, 10)

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    lp = LoginPage(driver)
    lp.load()
    lp.login("Admin","admin123")
    return driver