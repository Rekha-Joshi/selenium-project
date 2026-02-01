# Here we will define drivers and wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    """
    Base class for all page objects.
    Provides common WebDriver utilities such as clicking,
    typing, waiting for elements, and retrieving text.
    All other page classes inherit from this class.
    """
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
    
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def get_element(self, locator):
        return self.wait_visible(locator)
    
    def get_elements(self, locator):
        self.wait_present(locator)
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        element = self.wait_visible(locator)
        element.click()
    
    def type(self,locator, value: str, clear_first: bool=True):
        element = self.wait_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(value)
    
    def get_text(self, locator) -> str: #returns the visible text of the locator
        element = self.wait_visible(locator)
        return element.text
    
    def scroll_into_view(self, locator):
        element = self.wait_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element
