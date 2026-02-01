from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#define driver
driver = webdriver.Chrome()
driver.maximize_window()

#open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("Rekha Joshi")
driver.find_element(By.ID, "alertbtn").click()
#switch to alert 
alert = driver.switch_to.alert
print(alert.text)
assert "Rekha" in alert.text
alert.accept()
time.sleep(2)

driver.find_element(By.ID, "confirmbtn").click()
confirm = driver.switch_to.alert
alert.dismiss()
time.sleep(2)
driver.quit()
