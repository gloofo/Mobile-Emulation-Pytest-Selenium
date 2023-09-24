from src.modules import *
from src.source import *

@pytest.fixture(scope='session')
def setup():
    print("TEST SETUP")
    options = Options()
    options.add_argument("--hide-scrollbars")
    options.add_argument("--disable=infobars")
    devices = data()['devices']
    options.add_experimental_option("mobileEmulation", devices)

    url = data()['base']
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)

    yield driver
    
    print("TEST TEARDOWN")