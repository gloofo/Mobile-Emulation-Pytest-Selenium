import sys
sys.path.append('.')
from src.module import *

def test_surfWeb(setup, device):
    sleep(1)
    element = setup.find_element(By.CSS_SELECTOR, data()['page']['search'])
    element.send_keys("What is Fish?")
    element.send_keys(Keys.RETURN)
    sleep(2)