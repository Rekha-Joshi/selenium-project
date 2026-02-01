from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#define driver
driver = webdriver.Chrome()
driver.maximize_window()

#define implicit wait
driver.implicitly_wait(5) #wait for max 5 secs. Applied all over
wait = WebDriverWait(driver,10)

#open url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#search for keyword 'ber'
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
expected_items = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_items = []
# wait till search results appears and are visible. Return the list of web elements
wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='products']/div"))
)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
#loop through the result to find button to add to cart.
for item in products:
    actual_items.append(item.find_element(By.XPATH, "h4").text)
    button = item.find_element(By.XPATH, ".//button")
    wait.until(EC.element_to_be_clickable((By.XPATH, ".//button")))
    button.click()
print(f"Actual items: {actual_items}")
assert actual_items == expected_items

#click on cart icon and on. button - proceed to checkout
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#validate that sum is correct
items = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for item in items:
    sum = sum + int(item.text)
print(f"Total Amount: {sum}")
total_amount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert sum == total_amount

#enter promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

#do explicit wait to check if promo is applied
code_applied = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Code applied')]")))

assert 'Code applied' in code_applied.text

#validate total after discount is less than total amount
discount_amount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert discount_amount < float(total_amount)

driver.quit()