import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import yaml
import random

def data():
    with open("src/data.yaml","r") as file:
        getyaml = yaml.load(file, Loader=yaml.FullLoader)
    return getyaml

