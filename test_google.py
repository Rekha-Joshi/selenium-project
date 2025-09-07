from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


#auto manage chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://google.com") #open brwoser
print(driver.title) #print the title
assert "Google" in driver.title #check if title has word "Google"
driver.quit() #close browser