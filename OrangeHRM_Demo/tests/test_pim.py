import pytest
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage

def test_pim(logged_in_driver):
    driver = logged_in_driver
    dash = DashboardPage(driver)
    dash.is_loaded()
    dash.go_to_pim()
    assert PimPage(driver).is_loaded(), "PIM page did not load correctly."
