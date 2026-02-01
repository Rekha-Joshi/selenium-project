import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username, password", [
    ("admin","admin123"),
    ("user1", "wrongpass"),
    ("", "admin123")
    ])
def test_login(setup_browser, username, password):
    driver, wait = setup_browser
    print(f"Testing with username= '{username}' and password= '{password}'")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    print("driver id:", id(setup_browser[0]))

    # Example demo actions
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    username_input.clear()
    username_input.send_keys(username)
    password_input.clear()
    password_input.send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()