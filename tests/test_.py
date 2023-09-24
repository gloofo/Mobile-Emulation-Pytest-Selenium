import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from modules import *
from source import *

def test_surfWeb(setup, device):
    sleep(1)
    element = setup.find_element(By.CSS_SELECTOR, data()['page']['search'])
    element.send_keys("What is Fish?")
    element.send_keys(Keys.RETURN)
    sleep(2)