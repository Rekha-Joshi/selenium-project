#in this page, we will find the country, accept the terms, click on purchase and validate the success token
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ConfirmationPage():
    """
    Page object for the purchase confirmation page.
    Handles country selection, agreement checkbox,
    submitting the final purchase, and retrieving
    the success confirmation message.
    """