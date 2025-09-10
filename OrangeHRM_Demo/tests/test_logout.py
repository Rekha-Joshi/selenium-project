import pytest
from utils.driver_setup import get_driver
from pages.dashboard_page import DashboardPage

def test_logout_flow(logged_in_driver):
    driver = logged_in_driver
    dash = DashboardPage(driver)
    dash.logout()
    assert "/auth/login" in driver.current_url