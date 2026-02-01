from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME, "blinkingText").click()

#grab all windows in the list
windows = driver.window_handles

#switch to child window
driver.switch_to.window(windows[1])
full_text = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
print(full_text)

#grab the email
for word in full_text.split():
    if "@" in word:
        email = word
        break
print(email)
driver.close()

#switch back to main window
driver.switch_to.window(windows[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.ID, "signInBtn").click()
#grab the error text
el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger")))
print(el.text)
driver.quit()
