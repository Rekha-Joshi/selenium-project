from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

#define driver
driver = webdriver.Chrome()
driver.maximize_window()

#define wait
driver.implicitly_wait(5)

#open url
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

driver.switch_to.window(windows[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

driver.quit()