from src.module import *
from src.helper import *

creds = []

def register(driver):
    findElement(driver, 'nav', 'menu-btn', click=True)
    waitElement(driver, 'nav', 'sign-in')
    findElement(driver, 'nav', 'sign-in', click=True)
    waitElement(driver, 'register', 'panel')
    findElement(driver, 'register', 'main', click=True)
    waitElement(driver, 'register', 'form', 'main')

    #register with empty fields
    fillUpForm(driver, firstname=False)
    fillUpForm(driver, lastname=False)
    fillUpForm(driver, dob=False)
    fillUpForm(driver, address=False)
    fillUpForm(driver, postcode=False)
    fillUpForm(driver, city=False)
    fillUpForm(driver, state=False)
    fillUpForm(driver, country=False)
    fillUpForm(driver, phone=False)
    fillUpForm(driver, email=False)
    fillUpForm(driver, password=False)
    #with valid fields
    getCreds = fillUpForm(driver)
    creds.append(getCreds[0])
    creds.append(getCreds[1])

def login(driver):
    findElement(driver, 'register', 'form', 'email').send_keys(creds[0])
    findElement(driver, 'register', 'form', 'password').send_keys(creds[1])
    findElement(driver, 'register', 'submit', click=True)
    

