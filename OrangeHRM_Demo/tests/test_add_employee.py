import pytest
import time
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
    
@pytest.mark.parametrize( #with this one tests can run with multiple data
        "firstname, lastname", 
        [
            ("Ava", "Stone"),
            ("Liam", "Ng"),
            ("Maya", "Patel"),
        ]
)

def test_add_employee_multiple(logged_in_driver, firstname,lastname):
    driver = logged_in_driver
    dash = DashboardPage(driver)
    dash.go_to_pim()
    pim = PimPage(driver)
    assert pim.is_loaded(), "PIM page did not load correctly."
    pim.click_add()
    suffix = str(int(time.time()) % 10000)
    """
        time.time() → gives the current time in seconds since 1970 (e.g., 1725912345.123)
        int(...) → strips off the decimal → 1725912345
        % 10000 → takes just the last 4 digits → 2345
        str(...) → turns it into a string "2345"
    """
    pim.fill_basic_details(f"{firstname}-{suffix}",f"{lastname}-{suffix}")
    pim.save()
    try:
        assert pim.is_saved(), "Employee was not saved successfully"
    except AssertionError:
        logged_in_driver.save_screenshot("failed_add_employee.png")
        with open("failed_add_employee.html", "w", encoding="utf-8") as f:
            f.write(logged_in_driver.page_source)
        raise