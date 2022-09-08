from selenium.webdriver import Chrome, ActionChains
import pytest
from time import sleep

from selenium.webdriver.common.by import By


@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_register(setPath):
    driver.get("http://newtours.demoaut.com/")
    sleep(3)
    driver.maximize_window()

    driver.find_element(By.XPATH, "//a[contains(text(), 'REGISTER')]").click()
    sleep(2)

    driver.find_element(By.NAME, "firstName").send_keys("python")
    driver.find_element(By.NAME, "lastName").send_keys("selenium")
    driver.find_element(By.NAME, "phone").send_keys("12345676")
    driver.find_element(By.ID, "userName").send_keys("python@selenium.com")
    sleep(2)

    driver.find_element(By.NAME, "address1").send_keys("Main Road")
    driver.find_element(By.NAME, "city").send_keys("Wayne")
    driver.find_element(By.NAME, "state").send_keys("New Jersey")
    sleep(2)

    driver.find_element(By.NAME, "email").send_keys("python")
    driver.find_element(By.NAME, "password").send_keys("selenium")
    driver.find_element(By.NAME, "confirmPassword").send_keys("selenium")
    sleep(2)

    driver.find_element(By.NAME, "register").click()
    sleep(2)
