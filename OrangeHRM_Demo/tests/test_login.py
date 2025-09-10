import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_valid_login(logged_in_driver):
    driver = logged_in_driver
    print("\nTesting: Valid Login")
    assert "/dashboard" in driver.current_url
    h6 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h6"))
    )
    assert "Dashboard" in (h6.text or "")
    print("✅ Dashboard is visible after login")

def test_invalid_login(driver):
    print("/nTesting: Invalid Login")
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