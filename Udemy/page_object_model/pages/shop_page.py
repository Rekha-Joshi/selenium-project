# in this page, we will find out all the cards, find  the profuct to add, add to cart and click on checkout
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .checkout_page import CheckoutPage

class ShopPage(BasePage):
     """
    Page object for the product listing (Shop) page.
    Handles product-level actions such as locating items,
    adding a chosen product to the cart, and navigating
    to the checkout page.
    """
     PRODUCT_CARDS = (By.CSS_SELECTOR, "div.card.h-100")
     CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.nav-link.btn.btn-primary")

     def __init__(self,driver):
          super().__init__(driver)
     
     def add_product_to_cart(self, product_to_buy: str):
          products = self.get_elements(self.PRODUCT_CARDS)
          for product in products:
               product_name = product.find_element(By.CSS_SELECTOR, "div h4 a").text
               if product_name.strip().lower() == product_to_buy.strip().lower():
                    product.find_element(By.CSS_SELECTOR, "div button").click()
                    break
     def go_to_checkout(self) -> CheckoutPage:
          self.click(self.CHECKOUT_BUTTON)
          return CheckoutPage(self.driver)
