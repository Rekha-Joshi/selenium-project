from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#global varaibles
prodcut_to_buy = 'Blackberry'

#define driver
driver = webdriver.Chrome()
driver.maximize_window()

# define wait
wait = WebDriverWait(driver,10)

#open url
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

#loop through all products, find the right product and click on 'add to cart'
for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name.strip().lower() == prodcut_to_buy.strip().lower():
        product.find_element(By.XPATH, "div/button").click()

#click on checkout 1
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

#click on checkout 2
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

# enter 'f' on conuntry text box to search for list of countries
driver.find_element(By.ID, "country").send_keys("f") 

# Do explicit wait till item is visible
wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "France")))
driver.find_element(By.LINK_TEXT, "France").click()
driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click() #accept the term and conditions

#click on purchase button
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

#get the sucess text and assert
message = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
assert "Success! Thank you!" in message

driver.quit()
