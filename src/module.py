import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from faker import Faker
from datetime import datetime, timedelta
import yaml
import random

def phone():
    with open("resources/devices.yaml","r") as file:
        getData = yaml.load(file, Loader=yaml.FullLoader)
    return getData

def data(*keys):
    with open('resources/locators.yaml','r')  as file:
        getData = yaml.load(file, Loader=yaml.FullLoader)

    for locator in keys:
        getData = getData[locator]

    return getData

def fake():
    fake = Faker()
    return fake