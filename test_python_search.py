from selenium import webdriver
#webdriver → the remote control for browsers
from selenium.webdriver.common.by import By
# By → tells Selenium how to find an element (ID, NAME, XPATH, CSS)
from selenium.webdriver.chrome.service import Service
# Service → used to connect Selenium with ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait
# WebDriverWait → explicit wait (smart waiting)
from selenium.webdriver.support import expected_conditions as EC
# expected_conditions as EC → conditions like element is visible, title contains text
from webdriver_manager.chrome import ChromeDriverManager
# ChromeDriverManager → automatically downloads/updates the right driver
import pytest
# pytest → test runner we use to structure tests
import time

#auto manage chrome driver
@pytest.fixture #always write this for pytest.This is special function of python
#used to set up before test and clean up after test.
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit() #close browser

def test_python_search(driver):
    query = "getting started with python" #searching for this query
    driver.get("https://www.python.org") #open browser

    print(driver.title)

    #find the search box and type
    search_bar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"q")))
    search_bar.clear()
    search_bar.send_keys(query)
    search_bar.submit()
    time.sleep(5)

    print(driver.current_url)

    # wait until search results container appears
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".list-recent-events"))
    )

    # check if query text is present in the page source (not title)
    assert query.lower() in driver.page_source.lower()