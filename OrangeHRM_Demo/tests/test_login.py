import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    d = get_driver()
    yield d
    d.quit()

def test_valid_login(driver):
    page = LoginPage(driver)
    page.login("Admin","admin123")
    assert "/dashboard" in driver.current_url
    assert "Dashboard" in driver.page_source
    print("✅ Dashboard is visible after login")

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    print("Opened login page for invalid login test...")
    page.set_username("Admin")
    print("Entered username: Admin")
    page.set_password("wrongpass")
    print("Entered wrong password")
    page.submit()
    print("Clicked login button with invalid credentials")
    assert page.error_text() == "Invalid credentials"
    print("❌ Login failed as expected: Invalid credentials shown")