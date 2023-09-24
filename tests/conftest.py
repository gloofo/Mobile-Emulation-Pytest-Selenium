import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from modules import *
from source import *

def pytest_addoption(parser):
    parser.addoption("--device", action="store", default=None)

@pytest.fixture(scope='session')
def device(request):
    return request.config.getoption("device")

@pytest.fixture(scope='session')
def setup(device):
    print("TEST SETUP")
    options = Options()
    options.add_argument("--hide-scrollbars")
    #randomly pick a device name in the yaml file
    devices = data()['deviceName']
    getRandom = random.choice(devices)

    #if device name is not given in the command-line condition
    if device:
        options.add_experimental_option("mobileEmulation", {"deviceName": device})
    else:
        options.add_experimental_option("mobileEmulation", {"deviceName": getRandom})

    try:
        url = data()['base']
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(url)
        driver.execute_script("return document.readyState == 'complete';")

        yield driver
        driver.quit()
        print("TEST TEARDOWN")

    except Exception as e:
        print(e)

    

