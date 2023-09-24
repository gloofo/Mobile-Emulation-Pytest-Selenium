import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

@pytest.fixture
def driver(request):
    # Set up Chrome options for mobile emulation
    mobile_emulation = {
        "deviceName": "iPad Mini"
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    return driver

def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    sleep(5)
