from src.module import *

def findElement(driver, *keys, click=False):
    locator = data(*keys)
    element = driver.find_element(By.CSS_SELECTOR, locator)
    if click:
        element.click()
    else:
        return element

def findAllElements(driver, *keys):
    locator = data(*keys)
    element = driver.find_elements(By.CSS_SELECTOR, locator)
    return element

def waitElement(driver, *keys):
    locator = (By.CSS_SELECTOR, data(*keys))
    element = WebDriverWait(driver, 10)
    element.until(EC.visibility_of_element_located(locator))
    return element

def fillUp(driver, *keys, generate=None):
    generator = Faker()
    locator = data('register', *keys)
    element = driver.find_element(By.CSS_SELECTOR, locator)
    if generate == 'date_of_birth':
        element.send_keys(getattr(generator, generate)().strftime("%m%d%Y"))
    else:
        element.send_keys(getattr(generator, generate)())

def fillUpForm(
        driver, email=True, firstname=True, lastname=True,
        dob=True, address=True, postcode=True, city=True,
        state=True, country=True, phone=True, password=True
        ):
    
    getEmail = fake().email()
    getPassword = fake().password()
    form_data = {
        0: ('firstname', 'first_name'),
        1: ('lastname', 'last_name'),
        2: ('dob', 'date_of_birth'),
        3: ('address', 'address'),
        4: ('postcode', 'zipcode'),
        5: ('city', 'city'),
        6: ('state', 'state'),
        7: ('country', 'country'),
        8: ('phone', 'msisdn'),
        9: ('email', 'email'),
        10: ('password', 'password')
    }
    if not email:
        del form_data[9]
    if not firstname:
        del form_data[0]
    if not lastname:
        del form_data[1]
    if not dob:
        del form_data[2]
    if not address:
        del form_data[3]
    if not postcode:
        del form_data[4]
    if not city:
        del form_data[5]
    if not state:
        del form_data[6]
    if not country:
        del form_data[7]
    if not phone:
        del form_data[8]
    if not password:
        del form_data[10]
    for key, value in form_data.values():
        if key == 'password' and value == 'password':
                locator = data('register', 'form', 'password')
                element = driver.find_element(By.CSS_SELECTOR, locator)
                element.send_keys(getPassword)
        elif key == 'email' and value == 'email':
                locator = data('register', 'form', 'email')
                element = driver.find_element(By.CSS_SELECTOR, locator)
                element.send_keys(getEmail)
        else:
            fillUp(driver, 'form', key, generate=value)

    findElement(driver, 'register', 'form', 'register', click=True)
    sleep(2)
    validation = driver.execute_script('return document.querySelectorAll(".alert.alert-danger").length;')
    ageValidation = driver.execute_script('return document.getElementsByClassName("help-block").length;')

    if validation > 0 and ageValidation == 0:
        driver.refresh()
    elif validation == 1 and ageValidation == 1:
        date = findElement(driver, 'register', 'form', 'dob')
        date.send_keys(fake().date(pattern='%m%d%Y', end_datetime=datetime.now() - timedelta(days=18*365)))
        findElement(driver, 'register', 'form', 'register', click=True)
        waitElement(driver, 'register', 'panel')

    return getEmail, getPassword

