from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[contains(.,'Veg')]").click()

sorted_veg_fruit_list = []
veg_fruit_list = driver.find_elements(By.XPATH, "//tr/td[1]")
for veg_fruit in veg_fruit_list:
    sorted_veg_fruit_list.append(veg_fruit.text)

print(sorted_veg_fruit_list)
original_sorted_list = sorted_veg_fruit_list.copy()
print(original_sorted_list)
assert original_sorted_list == sorted(sorted_veg_fruit_list)

driver.quit()
