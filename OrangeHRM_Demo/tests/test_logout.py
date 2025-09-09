import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def driver():
    d = get_driver()
    yield d
    d.quit()

def test_logout_flow(driver):
    LoginPage(driver).login("Admin","admin123")
    dash = DashboardPage(driver)
    dash.logout()
    assert "/auth/login" in driver.current_url