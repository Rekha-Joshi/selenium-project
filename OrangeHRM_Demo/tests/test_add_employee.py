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
    
def test_add_employee(driver):
    LoginPage(driver).login("Admin","admin123")
    dash = DashboardPage(driver)
    dash.go_to_pim()
    pim = PimPage(driver)
    pim.assert_loaded()
    pim.click_add()
    pim.fill_basic_details("Rekha", "Test")
    pim.save()
    pim.assert_saved()