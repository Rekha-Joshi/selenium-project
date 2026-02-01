from optparse import Option
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") # 👈 runs without opening browser window
options.add_argument("--window-size=1920,1080") # optional but recommended
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options = options)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#scroll to the bottom of the screen
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(1)
#scrolling to the the middle. can give any number.0 means it's starting from the top.
driver.execute_script("window.scrollBy(0,500);")
time.sleep(1)

#take screenshot
driver.get_screenshot_as_file("screen.png")
driver.quit()