from selenium.webdriver import Firefox
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def browser():
    global driver
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r"C:\\Users\\zeyne\\Documents\\drivers\\geckodriver")
    driver.implicitly_wait(5)
    yield
    driver.quit()

def test_verify_title(browser):
     driver.get("https://app.hubspot.com/login")
     print("Headless Firefox Initialized")
     sleep(5)
     assert driver.title == "HubSpot Login"

def test_login_page(browser):
    driver.get("https://app.hubspot.com/login")
    print("Headless Firefox Initialized")
    sleep(5)
    driver.maximize_window()
    driver.find_element(By.ID, "username").send_keys("sammy@sample.com")
    sleep(2)
    driver.find_element(By.ID, "password").send_keys("test12345")
    sleep(2)
    driver.find_element(By.ID, "loginBtn").click()
    sleep(2)

