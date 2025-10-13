from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

#install and create instance of webriver

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)

#Enter data , click submit and print success message
driver.find_element(By.NAME, "name").send_keys("Rekha Joshi")
driver.find_element(By.NAME, "email").send_keys("test@email.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
#entering DOB and validating it
dob = driver.find_element(By.NAME, "bday")
dob.clear()
dob.send_keys("2017-12-12")
valid = driver.execute_script("return arguments[0].checkValidity();", dob)
print(f"Valid? {valid}")

#static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

#custom xpath
#//tagname[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hey!")

driver.quit()
