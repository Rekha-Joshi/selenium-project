from pages.home_page import HomePage
from pages.shop_page import ShopPage

def test_home_to_shop(setup_browser, base_url):
    driver = setup_browser #get the driver from fixture
    driver.get(base_url) # get_url gives the url name. we are opening ir here

    home = HomePage(driver)
    shop = home.go_to_shop()

    #sanity check
    assert isinstance(shop, ShopPage)
