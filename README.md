### What does this thing do?

-- Automates the following:
- User registration
  - Verifies validation of each field.
  - Verifies age if < 18.
- User Login

-- Please refer to Tool Shop url:
https://practicesoftwaretesting.com/


### Project Dependencies
---------------------

- *`pyyaml`*
- *`pytest`*
- *`Faker`*
- *`selenium`*


### Installation
---------------------
**Clone repository**
> git clone https://github.com/gloofo/Mobile-UI-Tool-Shop-Automation

**Install dependencies:**
> pip install -r requirements.txt

Run:
- Selects random device name if not given:
> pytest -v -rA
- Run on a specific device name:
> pytest -v -rA --device "Device Name Here"

``
Note: If you ever encounter an error running the command
it means that the emulated device cannot run the script.
``\
``example error: Message: invalid argument: cannot parse capability: goog:chromeOptions or InvalidArgumentException``\
\
``to solve this, just re-run the command``
 
