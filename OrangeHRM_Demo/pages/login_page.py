from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    ERROR_MSG = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def __init__(self,driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def load(self):
        print("Opening OrangeHRM login page...")
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        print("Login page loaded successfully.")
    
    def set_username(self, username: str):
        print(f"Entering username: {username}")
        el = self.wait.until(EC.element_to_be_clickable(self.USERNAME))
        el.clear()
        el.send_keys(username)
    
    def set_password(self, password: str):
        print("Entering password: ******")
        el = self.wait.until(EC.element_to_be_clickable(self.PASSWORD))
        el.clear()
        el.send_keys(password)
    
    def submit(self):
        print("Clicking on Login button...")
        self.driver.find_element(*self.LOGIN_BTN).click()
    
    def error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG)).text
    
    def login(self, username: str, password: str):
        self.load()
        self.set_username(username)
        self.set_password(password)
        self.submit()
        self.wait.until(EC.url_contains("/dashboard"))
        print("Login successful, dashboard page opened.")