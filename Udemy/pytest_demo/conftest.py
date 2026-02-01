from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest

def pytest_addoption(parser): #this lets you add your own command line arguments
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests"
    )

@pytest.fixture()
def setup_browser(request): #request is built in pytest fixture that provides context about current running test
    browser_name = request.config.getoption("browser") #reading the command line option
    print("\n [SETUP] Opening browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported Browser")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    print("\n [TEARDOWN] Closing browser")
    driver.quit()