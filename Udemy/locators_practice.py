from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#define driver
driver = webdriver.Chrome()
driver.maximize_window()

#open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#get all checkboxes and then loop over to click on option 2
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() #checking if checkbox is clicked
        break
time.sleep(2)
#get all radio buttons and then loop over to click on radio option 3
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()
        assert radiobutton.is_selected()
time.sleep(2)

#checking if text is displayed on the screen
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(2)

driver.quit()