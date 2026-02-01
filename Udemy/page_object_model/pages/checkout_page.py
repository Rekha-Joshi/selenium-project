#in this page, we will clickout on checkout and otional action is to remove the item
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage():
    """
    Represents the checkout page where cart items
    are reviewed. Provides actions to proceed to the
    final confirmation and purchase step.
    """