from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    HEADER = (By.TAG_NAME, "h6") #should contain Dashboard
    USER_MENU = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT = (By.CSS_SELECTOR, "a[href*='logout']")
    #constants for pim page
    PIM_MENU = (By.CSS_SELECTOR, "a[href*='pim']")
    SIDEBAR = (By.CSS_SELECTOR,"aside.oxd-sidepanel")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def assert_loaded(self):
        h6 = self.wait.until(EC.visibility_of_element_located(self.HEADER))
        assert "Dashboard" in h6.text
        print("On Dashboard page.")
    
    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_MENU)).click()
        print("Opened user menu.")
    
    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()
        print("Clicked logout.")
    
    def logout(self):
        self.assert_loaded()
        self.open_menu()
        self.click_logout()
        #back on login page
        self.wait.until(EC.url_contains("/auth/login"))
        print("Returned to login page.")
    
    def go_to_pim(self):
        self.wait.until(EC.visibility_of_element_located(self.SIDEBAR))
        self.wait.until(EC.element_to_be_clickable(self.PIM_MENU)).click()
        print("Clicked PIM in sidebar.")