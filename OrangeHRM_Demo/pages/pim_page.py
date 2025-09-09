from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PimPage():
    HEADER = (By.TAG_NAME,"h6") #should contain pim
    #add employee
    ADD_BTN = (By.XPATH,"//a[text()='Add Employee']")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME,"lastName")
    SAVE_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_TOAST = (By.XPATH, "//p[contains(.,'Success')]")
    PERSONAL_DETAILS_HEADER = (By.TAG_NAME, "h6")  # should show "Personal Details"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def assert_loaded(self):
        h6 = self.wait.until(EC.visibility_of_element_located(self.HEADER))
        assert "PIM" in h6.text
        assert "/pim/" in self.driver.current_url
        print("On PIM page (header + url verified).")
    
    def click_add(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BTN)).click()
        print("Clicked Add Employees.")
        self.wait.until(EC.url_contains("addEmployee"))
        assert "addEmployee" in self.driver.current_url
        print("On Add Employee page.")
    
    def fill_basic_details(self, firstname: str, lastname: str):
        print("Entering First Name.")
        ae_fn = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        ae_fn.clear()
        ae_fn.send_keys(firstname)
        print("Entering Last Name.")
        ae_ln = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME))
        ae_ln.clear()
        ae_ln.send_keys(lastname)
    
    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()
        print("Clicked on save button")
    
    def assert_saved(self):
        try:
            toast = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
            assert "Success" in toast.text
            print("Success toast visisble.")
            return
        except TimeoutException:
            self.wait.until(EC.url_contains("viewPersonalDetails"))
            h6 = self.wait.until(EC.visibility_of_element_located(self.PERSONAL_DETAILS_HEADER))
            assert "Personal Details" in h6.text
            print("Redirected to Personal Details page.")

        