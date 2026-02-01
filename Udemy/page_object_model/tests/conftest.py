import pytest
from selenium import webdriver

def pytest_addoption(parser): # this lets you add your own command line argument
    parser.addoption(
        "--browser",
        action = "store",
        default = "chrome",
        help = "Browser to run tests"
    )

@pytest.fixture()
def setup_browser(request): #request is built in pytest fixture that provides context about current running test
    browser = request.config.getoption("browser") #reading command line option
    print("\n [SETUP] Opening Browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise(ValueError, "Unsupported Browser")
    driver.maximize_window()
    yield driver
    print("\n [TEARDOWN] Closing Browser")
    driver.quit()

@pytest.fixture()
def base_url():
    return "https://rahulshettyacademy.com/angularpractice"