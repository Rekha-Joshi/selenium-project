from selenium import webdriver #it's like remote control for browsers
from selenium.webdriver.chrome.service import Service #connect selenium with driver
from selenium.webdriver.chrome.options import Options # add options
from webdriver_manager.chrome import ChromeDriverManager #automatically updates right driver

def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
