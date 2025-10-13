import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service

#from webdriver_manager.chrome import ChromeDriverManager

#install and get driver handle
#driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.maximize_window()

#open url
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
#find elements return list of web elements
print(len(countries))
for country in countries:
    if country.text == 'India':
        country.click()
        break
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

driver.quit()