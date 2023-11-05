from src.module import *

def pytest_addoption(parser):
    parser.addoption("--device", action="store", default=None)

@pytest.fixture(scope='session')
def device(request):
    return request.config.getoption("device")

@pytest.fixture(scope='session')
def driver(device):
    #setup
    options = Options()
    options.add_argument("--hide-scrollbars")
    devices = phone()['deviceName']
    getRandom = random.choice(devices)

    if device:
        options.add_experimental_option("mobileEmulation", {"deviceName": device})
    else:
        options.add_experimental_option("mobileEmulation", {"deviceName": getRandom})

    driver = webdriver.Chrome(options=options)
    driver.get(data('base'))
    yield driver
    #teardown
    driver.close()
    driver.quit()


