from src.module import *
from src.main import *

def test_register(driver, device):
    register(driver)

def test_login(driver):
    login(driver)