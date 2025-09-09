import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage

@pytest.fixture
def driver():
    d = get_driver()
    yield d
    d.quit()

def test_pim(driver):
    LoginPage(driver).login("Admin","admin123")
    dash = DashboardPage(driver)
    dash.assert_loaded()
    dash.go_to_pim()
    PimPage(driver).assert_loaded()
