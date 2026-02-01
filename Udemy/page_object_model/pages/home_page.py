# In this file, we will go to the url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .shop_page import ShopPage

class HomePage(BasePage):
    """
    Represents the landing page of the application.
    Responsible for high-level navigation actions such as
    opening the Shop page from the home screen.
    """
    # locaotr for shop button
    #method - go_to_shop()
        #wait -> click
        #return ShopPage object
    SHOP_LINK = (By.LINK_TEXT, "Shop")

    def __init__(self, driver):
        super().__init__(driver)
    
    def go_to_shop(self):
        self.click(self.SHOP_LINK)
        return ShopPage(self.driver) #retruning ShopPage object. this shows we moved to next page