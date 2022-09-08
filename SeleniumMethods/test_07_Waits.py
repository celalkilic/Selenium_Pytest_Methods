from selenium.webdriver import Firefox
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\geckodriver"
    driver =Firefox(executable_path=path)
    yield
    driver.quit()

def test_explicitly_wait(setPath):
    driver.maximize_window()
    driver.get("https://app.hubspot.com/login")

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID,"username").send_keys("sample@gmail.com")
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "password")))
    driver.find_element(By.ID,"password").send_keys("123456")
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "loginBtn")))
    driver.find_element(By.ID,"loginBtn").click()

    #implicitly wait
    driver.implicitly_wait(20)
    driver.implicitly_wait(20)